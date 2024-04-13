from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSizePolicy

from gui.dict_list_panel import DictListPanel
from gui.player_panel import PlayerPanel


class LearnTab(QWidget):
    def __init__(self):
        super().__init__()
        main_layout = QHBoxLayout()
        dict_list = DictListPanel('../output')
        dict_list.setMaximumHeight(400)
        dict_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        dict_list.itemSelected.connect(self.refresh_dict_items)
        main_layout.addWidget(dict_list, stretch=1, alignment=Qt.AlignTop)
        self.player_panel = PlayerPanel()
        main_layout.addWidget(self.player_panel, stretch=2)
        self.setLayout(main_layout)

    def refresh_dict_items(self, name):
        print("Selected name111: %s" % name)
        self.player_panel.refresh_dict_items(name)