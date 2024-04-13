from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout

from crawler.crawler import DictCrawler
from model.dict import DictModel
from model.filemanager import FileManager


class EnterLinkTab(QWidget):
    def __init__(self):
        super().__init__()
        description = QLabel()
        description.setText("Enter crawl link into input field and click Go! button. All output file will appear in "
                            "output folder.")
        self.input = QLineEdit()
        action = QPushButton("Go!")
        action.clicked.connect(self.on_crawl)
        self.table_view = QTableView()
        layout = QHBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(action)
        layout2 = QVBoxLayout()
        layout2.addWidget(description)
        layout2.addLayout(layout)
        layout2.addWidget(self.table_view)
        self.setLayout(layout2)

    def on_crawl(self):
        crawler = DictCrawler(self.input.text())
        crawler.crawl()
        data = FileManager(crawler.name).get_dataframe()
        self.table_view.setModel(DictModel(data))