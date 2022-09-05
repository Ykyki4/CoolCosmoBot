import requests


def download_image(path, file_url, params):
    response = requests.get(file_url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)