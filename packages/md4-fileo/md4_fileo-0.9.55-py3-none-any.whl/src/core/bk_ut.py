from loguru import logger
from typing import TYPE_CHECKING

from PyQt6.QtCore import (Qt, QModelIndex, pyqtSlot, QPoint, QThread,
    QTimer,
)
from PyQt6.QtGui import (QAction, QResizeEvent,
)
from PyQt6.QtWidgets import QMenu, QTreeView

from . import (app_globals as ag, low_bk, load_files,
    drag_drop as dd, icons,
)
from ..widgets import workers, find_files

if TYPE_CHECKING:
    from .sho import shoWindow

self: 'shoWindow' = None

def save_bk_settings():
    if not ag.db.conn:
        return

    actions = ag.field_menu.menu().actions()

    try:
        curr_dir_idx = ag.dir_list.currentIndex()
        settings = {
            "FIELDS_STATE": [int(a.isChecked()) for a in actions],
            "COLUMN_WIDTH": low_bk.get_columns_width(),
            "TAG_SEL_LIST": low_bk.tag_selection(),
            "EXT_SEL_LIST": low_bk.ext_selection(),
            "AUTHOR_SEL_LIST": low_bk.author_selection(),
            "FILE_SORT_COLUMN": ag.file_list.model().sortColumn(),
            "FILE_SORT_ORDER": ag.file_list.model().sortOrder(),
            "SHOW_HIDDEN": int(self.show_hidden.isChecked()),
            "HISTORY": ag.history.get_history(),
        }
        ag.save_settings(**settings)
        low_bk.save_file_row(ag.file_list.currentIndex().row(), curr_dir_idx)
        self.filter_setup.save_filter_settings()
    except:
        pass

@pyqtSlot()
def search_files():
    ff = find_files.findFile(ag.app)
    ff.move(ag.app.width() - ff.width() - 40, 40)
    ff.show()
    ff.srch_pattern.setFocus()

@pyqtSlot(bool)
def toggle_collapse(collapse: bool):
    if collapse:
        low_bk.save_branch_in_temp(ag.dir_list.currentIndex())
        ag.dir_list.collapseAll()
    else:
        idx = low_bk.restore_branch_from_temp()
        ag.dir_list.setCurrentIndex(idx)

def bk_setup(main: 'shoWindow'):
    ag.file_list.resizeEvent = file_list_resize_0
    low_bk.dir_list_setup()
    ag.file_list.currentChanged = current_file_changed

    set_context_menu()

    if ag.db.conn:
        populate_all()

        QTimer.singleShot(10 * 1000, show_lost_files)
        QTimer.singleShot(5 * 60 * 1000, run_update0_files)
        QTimer.singleShot(15 * 60 * 1000, run_update_touched_files)
        QTimer.singleShot(25 * 60 * 1000, run_update_pdf_files)

    dd.set_drag_drop_handlers()

    ag.signals_.start_file_search.connect(file_loading)
    ag.signals_.app_mode_changed.connect(low_bk.app_mode_changed)

    ag.tag_list.edit_item.connect(low_bk.tag_changed)
    ag.author_list.edit_item.connect(low_bk.author_changed)
    ag.tag_list.delete_items.connect(low_bk.delete_tags)
    ag.author_list.delete_items.connect(low_bk.delete_authors)

    ag.file_list.doubleClicked.connect(
        lambda: ag.signals_.user_signal.emit("double click file"))

def set_field_menu():
    checked = ag.get_setting("FIELDS_STATE", (1, 1, *((0,)*8)))
    fields = (
        'File Name', 'Open Date', 'rating', 'Open#', 'Modified',
        'Pages', 'Size', 'Published', 'Date of last note', 'Created',
    )
    tool_tips = (
        ",Last opening date,rating of file,number of file openings,"
        "Last modified date,Number of pages(in book),Size of file,"
        "Publication date(book),Date of last note,File creation date"
    )

    menu = QMenu(self)
    for field,ch,tt in zip(fields, checked, tool_tips.split(',')):
        act = QAction(field, self, checkable=True)
        if tt:
            act.setToolTip(tt)
        act.setChecked(int(ch))
        act.triggered.connect(lambda state, fld=field: field_list_changed(state, field=fld))
        menu.addAction(act)

    menu.actions()[0].setEnabled(False)
    menu.setToolTipsVisible(True)
    ag.field_menu.setMenu(menu)

@pyqtSlot()
def click_setup_button():
    menu = QMenu(self)
    if not ag.single_instance:
        menu.addAction('New window/ ')
        menu.addSeparator()
    menu.addAction('Report duplicate files')
    menu.addSeparator()
    menu.addAction('Preferences')
    menu.addSeparator()
    menu.addAction('About')
    sz = menu.sizeHint()
    pos = self.ui.btnSetup.pos()
    action = menu.exec(ag.app.mapToGlobal(
        pos + QPoint(53, 26 - sz.height())
    ))
    if action:
        ag.signals_.user_signal.emit(f"Setup {action.text()}")

def field_list_changed(state, field):
    idx = ag.file_list.currentIndex()

    low_bk.refresh_file_list()
    low_bk.set_current_file(idx.row())

@pyqtSlot(QModelIndex, QModelIndex)
def current_file_changed(curr: QModelIndex, prev: QModelIndex):
    if curr.isValid():
        ag.file_list.scrollTo(curr)
        self.ui.current_filename.setText(low_bk.file_name(curr))
        low_bk.file_notes_show(curr)

def file_list_resize_0(e: QResizeEvent):
    if ag.db.conn:
        restore_dirs()

    ag.file_list.resizeEvent = low_bk.file_list_resize
    super(QTreeView, ag.file_list).resizeEvent(e)

def restore_dirs():
    low_bk.set_dir_model()
    ag.filter_dlg.restore_filter_settings()
    restore_history()

def populate_all():
    if not ag.db.conn:
        return

    low_bk.populate_tag_list()
    low_bk.populate_ext_list()
    low_bk.populate_author_list()

    hide_state = ag.get_setting("SHOW_HIDDEN", 0)
    self.show_hidden.setChecked(hide_state)
    self.show_hidden.setIcon(icons.get_other_icon("show_hide", hide_state))

def restore_history():
    restore_sorting()
    hist = ag.get_setting('HISTORY', [[], [], []])  # next_, prev, curr
    ag.history.set_history(*hist)

    idx = low_bk.expand_branch(ag.history.get_current())
    if idx.isValid():
        ag.dir_list.setCurrentIndex(idx)
    else:
        low_bk.show_folder_files()

def restore_sorting():
    col = ag.get_setting("FILE_SORT_COLUMN", 0)
    order = ag.get_setting("FILE_SORT_ORDER", Qt.SortOrder.AscendingOrder)
    ag.file_list.header().setSortIndicator(col, order)

@pyqtSlot()
def show_hidden_dirs():
    """
    QCheckBox stateChanged signal handler
    """
    branch = low_bk.define_branch(ag.dir_list.currentIndex())
    low_bk.set_dir_model()
    idx = low_bk.expand_branch(branch)
    ag.dir_list.setCurrentIndex(idx)

def set_context_menu():
    """
    Set context menus for each widget
    :return:
    """
    ag.dir_list.customContextMenuRequested.connect(dir_menu)
    ag.file_list.customContextMenuRequested.connect(file_menu)

@pyqtSlot(QPoint)
def dir_menu(pos):
    idx = ag.dir_list.indexAt(pos)
    menu = QMenu(self)
    if idx.isValid():
        menu.addSeparator()
        menu.addAction("Delete folder(s)")
        menu.addSeparator()
        menu.addAction("Toggle hidden state")
        menu.addSeparator()
        menu.addAction("Import files")
        menu.addSeparator()
        menu.addAction("Create folder")
        menu.addAction("Create folder as child")
    else:
        menu.addAction("Create folder")

    action = menu.exec(ag.dir_list.mapToGlobal(pos))
    if action:
        ag.signals_.user_signal.emit(f"Dirs {action.text()}")

@pyqtSlot(QPoint)
def file_menu(pos):
    idx = ag.file_list.indexAt(pos)
    if idx.isValid():
        menu = QMenu(self)
        menu.addAction("Copy file name(s)")
        menu.addAction("Copy full file name(s)")
        menu.addAction("Reveal in explorer")
        menu.addSeparator()
        menu.addAction("Open file")
        menu.addSeparator()
        menu.addAction("Rename file")
        menu.addSeparator()
        menu.addAction("Export selected files")
        menu.addSeparator()
        menu.addAction("Remove file(s) from folder")
        menu.addSeparator()
        menu.addAction("Delete file(s) from DB")
        action = menu.exec(ag.file_list.mapToGlobal(pos))
        if action:
            ag.signals_.user_signal.emit(f"Files {action.text()}")

@pyqtSlot(str, list)
def file_loading(root_path: str, ext: list[str]):
    """
    search for files with a given extension
    in the selected folder and its subfolders
    """
    if self.is_busy or not ag.db.conn:
        return
    self.thread = QThread(self)

    self.worker = load_files.loadFiles()
    self.worker.set_files_iterator(load_files.yield_files(root_path, ext))
    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.load_data)
    self.worker.finished.connect(finish_loading)
    self.worker.finished.connect(self.worker.deleteLater)

    self.thread.start()
    self.set_busy(True)

@pyqtSlot(bool)
def finish_loading(has_new_ext: bool):
    self.thread.quit()
    self.ui.btnScan.setEnabled(True)
    self.set_busy(False)
    if has_new_ext:
        ag.signals_.user_signal.emit("ext inserted")
    low_bk.reload_dirs_changed(ag.dir_list.currentIndex())

@pyqtSlot()
def show_lost_files():
    workers.find_lost_files()

@pyqtSlot()
def run_update0_files():
    """
    collect data about recently loaded files
    """
    run_worker(workers.update0_files)

@pyqtSlot()
def run_update_touched_files():
    """
    update the data of files opened since the last update
    """
    run_worker(workers.update_touched_files)

@pyqtSlot()
def run_update_pdf_files():
    """
    collect specifict data about recently loaded pdf files
    """
    run_worker(workers.update_pdf_files)

def run_worker(func):
    if self.is_busy or not ag.db.conn:
        return
    self.thread = QThread(self)

    self.worker = workers.worker(func)
    self.worker.moveToThread(self.thread)

    self.thread.started.connect(self.worker.run)
    self.worker.finished.connect(finish_worker)
    self.worker.finished.connect(self.worker.deleteLater)

    self.thread.start()
    self.set_busy(True)

@pyqtSlot()
def finish_worker():
    self.thread.quit()
    self.set_busy(False)
