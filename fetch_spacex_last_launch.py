import requests


from pathlib import Path
from file_download import file_download
from argparser import arg_parser


args = arg_parser()
launch_id = args.launch_id
spacex_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"


def fetch_spacex_last_launch(url):
    params=None
    response = requests.get(url)
    response.raise_for_status()
    file_urls = response.json().get('links').get('flickr').get('original')
    for n, file_url in enumerate(file_urls):
        filename = f'spacex_{n}.jpg'
        Path('images/').mkdir(parents=True, exist_ok=True)
        path = f'images/{filename}'
        file_download(path, file_url, params)

fetch_spacex_last_launch(spacex_url)