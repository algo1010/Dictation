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