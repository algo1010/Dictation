from PySide6.QtWidgets import QWidget, QTableView, QVBoxLayout
from model.dict import DictModel
from model.filemanager import FileManager


class DictListItem(QWidget):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.table_view = QTableView()
        if name is not None:
            self.refresh(name)
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def refresh(self, name):
        data = FileManager(name).get_dataframe()
        data = data[["Content"]]
        self.table_view.setModel(DictModel(data))
        self.table_view.resizeColumnsToContents()
