import pygame
from threading import Thread
import time


class AudioPlayer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playing = False
        self.paused = False
        self.audio_thread = None

    def play_audio(self, file_path):
        if self.playing:
            self.stop_audio()
        self.audio_thread = Thread(target=self._play_audio_thread, args=(file_path,))
        self.audio_thread.start()

    def _play_audio_thread(self, file_path):
        self.playing = True
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            if not self.playing or self.paused:
                break
            time.sleep(0.1)
        self.playing = False

    def stop_audio(self):
        self.playing = False
        self.paused = False
        pygame.mixer.music.stop()

    def pause_audio(self):
        if self.playing and not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def resume_audio(self):
        if self.playing and self.paused:
            pygame.mixer.music.unpause()
            self.paused = False

    def play_audio_list(self, file_list, repeat_times=1, delay=1, is_repeat=False):
        for file_path in file_list:
            for _ in range(repeat_times):
                self.play_audio(file_path)
                while self.playing:
                    time.sleep(0.1)
                time.sleep(delay)

        if is_repeat:
            self.play_audio_list(file_list, repeat_times=repeat_times, delay=delay, is_repeat=is_repeat)

    def set_speed(self, speed):
        pygame.mixer.music.set_speed(speed)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)
