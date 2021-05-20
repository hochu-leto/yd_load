import requests
class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.OAuth = 'AQAAAAAAONHMAADLWwvS9ato0E0WnSlDhcPEv-s'
        self.ID = 'e323f17f6d1142ea8b84bf60a299ce4a'
        self.password = '97454d77308e497aa0976d9d8c0df1b9'
    def get_headers(self):
    	return { 'Content-Type':'application/json', 'Authorization':'OAuth {}'.format(self.OAuth)}
    	
    def upload(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        headers = self.get_headers()
        params = {'path':self.file_path, 'overwrite':'true'}
        response = requests.put(upload_url, headers=headers, params=params)
        print(response.json())
        return 'ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('/storage/emulated/0/Python/example_http_request.py')
    result = uploader.upload()

