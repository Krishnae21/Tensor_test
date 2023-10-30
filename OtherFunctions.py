import re
import requests

class Functions:
    @staticmethod
    def download_file(url: str):
        file_path = url[url.rfind(r'/') + 1:]
        response = requests.get(url)
        with open(file_path, "wb") as file:
            file.write(response.content)
        return response.content
