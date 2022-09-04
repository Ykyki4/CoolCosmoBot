import requests

def file_download(path, file_url, params):
    if params!=None:
        response = requests.get(file_url, params=params)
    else:
        response = requests.get(file_url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)