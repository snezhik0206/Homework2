import requests
import os


class YaUploader:
    def __init__(self, token):
        self.URL = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                        'Authorization': f'OAuth {token}'}
        self.filename = 'text.txt'
        self.replace = True

    def upload(self, file_path):
        res = requests.get(f"{self.URL}/upload?path={self.filename}&overwrite={self.replace}", headers=self.headers)\
            .json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res.get("href"), files={'file': f})
                print(res)
            except KeyError:
                print(res)


def main():
    if __name__ == '__main__':
        directory = os.getcwd()
        file_name = "test.txt"
        file_path = os.path.join(directory, file_name)
        with open('token.ini', 'r') as f:
            token = f.read().strip()
        uploader = YaUploader(token)
        uploader.upload(file_path)


main()
