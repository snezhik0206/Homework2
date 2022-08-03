import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path, URL='https://cloud-api.yandex.net/v1/disk/resources', replace=True):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        res = requests.get(f"{URL}/upload?path=test.txt&overwrite={replace}", headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                requests.put(res["href"], files={'file': f})
            except KeyError:
                print(res)


def main():
    if __name__ == '__main__':
        directory = os.getcwd()
        file_name = "test.txt"
        file_path = os.path.join(directory, file_name)
        token = ""
        uploader = YaUploader(token)
        uploader.upload(file_path)


main()
