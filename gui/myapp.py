import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, \
    QHBoxLayout, QCheckBox, QComboBox, QTextEdit, QTableView, QTabWidget, QTabBar

from gui.dict_list_panel import DictListPanel
from gui.enter_link_tab import EnterLinkTab
from gui.learn_tab import LearnTab


class CustomTabBar(QTabBar):
    def tabSizeHint(self, index):
        size_hint = super().tabSizeHint(index)
        size_hint.setHeight(40)  # Chiều cao tab
        size_hint.setWidth(120)  # Chiều rộng tab
        return size_hint


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dictation")
        self.resize(900, 600)

        tab_widget = QTabWidget()
        tab_widget.setTabBar(CustomTabBar())
        tab1 = EnterLinkTab()
        tab2 = LearnTab()
        tab_widget.addTab(tab1, "Crawl Dict")
        tab_widget.addTab(tab2, "Learn")
        self.setCentralWidget(tab_widget)


app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())
