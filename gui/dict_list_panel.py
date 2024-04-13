from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QFileSystemModel, QListView, QVBoxLayout, QWidget

# class DictListPanel(QWidget):
#     def __init__(self, path):
#         super().__init__()
#         self.path = path
#         self.model = QFileSystemModel()
#         self.model.setRootPath(path)
#
#         self.list_view = QListView()
#         self.list_view.setModel(self.model)
#         self.list_view.setRootIndex(self.model.index(path))
#         self.list_view.clicked.connect(self.on_item_clicked)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.list_view)
#         self.setLayout(layout)
#
#     def on_item_clicked(self, index):
#         selected_item = self.model.data(index, Qt.DisplayRole)
#         print("Selected Item:", selected_item)

from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListView, QFileSystemModel


class DictListPanel(QWidget):
    itemSelected = Signal(str)  # Tín hiệu tùy chỉnh chứa văn bản của mục được chọn

    def __init__(self, path):
        super().__init__()
        self.path = path
        self.model = QFileSystemModel()
        self.model.setRootPath(path)

        self.list_view = QListView()
        self.list_view.setModel(self.model)
        self.list_view.setRootIndex(self.model.index(path))

        layout = QVBoxLayout()
        layout.addWidget(self.list_view)
        self.setLayout(layout)

        # Kết nối tín hiệu itemSelectionChanged của QListView với phương thức xử lý của chúng ta
        self.list_view.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        # Lấy văn bản của mục được chọn
        selected_indexes = selected.indexes()
        if selected_indexes:
            selected_index = selected_indexes[0]
            selected_item_text = self.model.data(selected_index)
            # Phát ra tín hiệu với văn bản của mục được chọn
            self.itemSelected.emit(selected_item_text)
