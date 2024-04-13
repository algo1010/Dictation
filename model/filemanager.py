import os
import pandas as pd


class FileManager:
    def __init__(self, name):
        self.name = name
        self.base_path = '../output'

    def get_dataframe(self):
        folder_path = os.path.join(self.base_path, self.name)
        if not os.path.exists(folder_path):
            return None
        content_path = os.path.join(folder_path, 'content.csv')
        if not os.path.exists(content_path):
            return None
        df = pd.read_csv(content_path)
        return df

    def get_audios(self):
        folder_path = os.path.join(self.base_path, self.name)
        audio_path = os.path.join(folder_path, 'audio')
        if not os.path.exists(audio_path):
            return None
        paths = []
        for file_name in os.listdir(audio_path):
            if file_name.endswith(".mp3"):
                paths.append(os.path.join(audio_path, file_name))
        paths.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
        return paths
