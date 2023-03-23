
import requests



class YaUploader:
    def __init__(self, token: str):
        self.token = token

        
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load
    


    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url_to_load = self._get_upload_link(disk_file_path=file_path)
        response = requests.put(url_to_load, data=open(file_path, 'rb'))
       
        if response.status_code == 201:
            print("Загрузка файла выполнена")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_path = "vimis.txt"
    token = ""
    uploader = YaUploader(token)
    # result = uploader.upload(path_to_file)
    result = uploader.upload(file_path)
