import threading

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QCheckBox, QStackedWidget, QLabel, QPushButton, \
    QSpinBox

from audio.player import AudioPlayer
from gui.dict_list_items import DictListItem
from model.filemanager import FileManager


class PlayerPanel(QWidget):
    def __init__(self, name=None):
        super().__init__()
        self.name = name
        self.is_repeat = False
        self.audio_player = AudioPlayer()
        self.show_script = QCheckBox("Show script")
        self.show_script.setChecked(False)
        self.show_script.stateChanged.connect(self.on_show_script)
        self.dict_list = DictListItem(name)
        self.overlay = QLabel("Hidden scripts will help you to improve the performance of English listen skill")
        self.overlay.setStyleSheet('background-color: #263238;')
        self.stack = QStackedWidget()
        self.stack.addWidget(self.overlay)
        self.stack.addWidget(self.dict_list)

        self.player = QWidget()
        player_layout = QHBoxLayout()
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.on_play)
        player_layout.addWidget(self.play_button)

        repeat_checkbox = QCheckBox("Repeat")
        repeat_checkbox.setChecked(False)
        repeat_checkbox.stateChanged.connect(self.on_repeat)
        player_layout.addWidget(repeat_checkbox)

        repeat_content = QWidget()
        repeat_content.setFixedWidth(150)
        repeat_layout = QHBoxLayout()
        repeat_label = QLabel("# Repeat")
        repeat_layout.addWidget(repeat_label)
        self.no_repeat = QSpinBox()
        self.no_repeat.setMinimum(1)
        self.no_repeat.setMaximum(15)
        repeat_layout.addWidget(self.no_repeat)
        repeat_content.setLayout(repeat_layout)
        player_layout.addWidget(repeat_content)

        delay_content = QWidget()
        delay_content.setFixedWidth(200)
        delay_layout = QHBoxLayout()
        delay_label = QLabel("Delay in seconds")
        delay_layout.addWidget(delay_label)
        self.delay_spin = QSpinBox()
        self.delay_spin.valueChanged
        self.delay_spin.setMinimum(1)
        self.delay_spin.setMaximum(10)
        delay_layout.addWidget(self.delay_spin)
        delay_content.setLayout(delay_layout)
        player_layout.addWidget(delay_content)

        self.player.setLayout(player_layout)

        layout = QVBoxLayout()
        layout.addWidget(self.show_script)

        layout.addWidget(self.stack, 3)
        layout.addWidget(self.player, 1)
        self.setLayout(layout)

    def refresh_dict_items(self, name):
        self.name = name
        self.dict_list.refresh(name)

    def on_show_script(self, checked):
        if checked == Qt.Checked.value:
            self.dict_list.setVisible(True)
            self.overlay.setVisible(False)
        else:
            self.dict_list.setVisible(False)
            self.overlay.setVisible(True)

    def on_play(self):
        audio_thread = threading.Thread(target=self._play_audio_list)
        audio_thread.start()

    def on_repeat(self, state):
        self.is_repeat = state == Qt.Checked.value

    def _play_audio_list(self):
        file_manager = FileManager(self.name)
        paths = file_manager.get_audios()
        player = AudioPlayer()
        player.stop_audio()
        player.play_audio_list(file_list=paths, repeat_times=5, delay=0.5, is_repeat=self.is_repeat)