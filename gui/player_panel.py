from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QCheckBox

from gui.dict_list_items import DictListItem


class PlayerPanel(QWidget):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.show_script = QCheckBox("Show script")
        self.show_script.setChecked(False)
        self.show_script.stateChanged.connect(self.on_show_script)
        self.dict_list = DictListItem(name)
        self.dict_list.setVisible(False)
        self.player = QWidget()
        self.player.setStyleSheet('background-color: rgb(255, 255, 255);')
        layout = QVBoxLayout()
        layout.addWidget(self.show_script)
        layout.addWidget(self.dict_list, 3)
        layout.addWidget(self.player, 1)
        self.setLayout(layout)

    def refresh_dict_items(self, name):
        self.dict_list.refresh(name)

    def on_show_script(self, checked):
        print(checked)
