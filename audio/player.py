from pydub import AudioSegment
from pydub.playback import play
import time

# Load the audio file
audio = AudioSegment.from_file("audio.mp3", format="mp3")

# Play the audio
n = 5
while n > 0:
    play(audio)
    n = n-1
    time.sleep(1)

