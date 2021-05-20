import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.OAuth = '...'

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.OAuth)}

    def upload(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        headers = self.get_headers()
        params = {'path': self.file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        json_ = response.json()
        href_url = json_['href']
        response = requests.put(href_url)
        if str(response) == '<Response [201]>':
            return 'файл загружен на диск'
        else:
            return 'что-то пошло не так, ответ сервера ' + str(response)


if __name__ == '__main__':
    uploader = YaUploader(r'test_write.txt')
    result = uploader.upload()
    print(result)
