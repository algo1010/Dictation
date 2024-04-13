import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot
from pydub import AudioSegment
from pydub.playback import play as pb
import threading


@Slot()
def play():
    path = "../audio/audio.mp3"
    play_thread = threading.Thread(target=play_in_thread, args=(path,))
    play_thread.start()


def play_in_thread(path):
    audio = AudioSegment.from_file(path, format="mp3")
    pb(audio)


app = QApplication(sys.argv)
button = QPushButton('Play')
button.clicked.connect(play)
button.show()

app.exec()
