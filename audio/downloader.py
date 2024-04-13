import requests
import os


class AudioDownloader:
    def __init__(self, name, url, destination):
        self.url = url
        self.destination = destination
        self.name = name

    def download(self):
        response = requests.get(self.url)
        file_name = os.path.basename(self.url)
        file_extension = os.path.splitext(file_name)[1]
        file_path = os.path.join(self.destination, self.name + file_extension)
        with open(file_path, "wb") as file:
            file.write(response.content)
