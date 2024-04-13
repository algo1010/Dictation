from bs4 import BeautifulSoup
import requests
import json
import csv
import os

from audio.downloader import AudioDownloader


class DictCrawler:
    def __init__(self, url):
        self.url = url
        self.name = ''

    def crawl(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all("script")
        self.name = soup.find('main').find('h1').string.split("(Listen and Type)")[0].strip()
        for script in scripts:
            if "window.appGlobals" in str(script):
                self.__parse(script.string)
                break

    def __parse(self, content):
        json_string = self.__get_json_data(content)
        challenges = self.__get_challenges(json_string)
        self.__get_dicts(challenges)

    def __get_json_data(self, content):
        s = content.find('{')
        e = content.rfind('}')
        return content[s:e + 1]

    def __get_challenges(self, content):
        data = json.loads(content)
        return data['challenges']

    def __get_dicts(self, challenges):
        fields = ["Position", "Content", "Audio", "Start Time", "End Time"]
        csv_file = 'content.csv'
        folder_name = "output/" + self.name
        folder_path = "../" + folder_name
        audio_path = folder_path + '/audio'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if not os.path.exists(audio_path):
            os.makedirs(audio_path)
        file_path = os.path.join(folder_path, csv_file)
        with open(file_path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for challenge in challenges:
                row = {
                    "Position": challenge['position'],
                    "Content": challenge['content'],
                    "Audio": challenge['audioSrc'],
                    "Start Time": challenge['timeStart'],
                    "End Time": challenge['timeEnd'],
                }
                writer.writerow(row)
                downloader = AudioDownloader(
                    str(challenge['position']),
                    challenge['audioSrc'],
                    audio_path)
                downloader.download()


if __name__ == '__main__':
    url = "https://dailydictation.com/exercises/short-stories/4-going-camping.7/listen-and-type"
    crawler = DictCrawler(url)
    crawler.crawl()
