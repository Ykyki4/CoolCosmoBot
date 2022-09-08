import requests
import argparse


from pathlib import Path, PurePath
from file_download import download_image


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("launch_id")
    args = parser.parse_args()
    return args


def download_fetch_spacex_last_launch(launch_id, url):
    params=None
    response = requests.get(url)
    response.raise_for_status()
    images_urls = response.json().get('links').get('flickr').get('original')
    for number, image_url in enumerate(images_urls):
        filename = f'spacex_{number}.jpg'
        Path('images/').mkdir(parents=True, exist_ok=True)
        path = PurePath('images', filename)
        download_image(path, image_url, params)



if __name__ == "__main__":
    launch_id = arg_parser().launch_id # 5eb87d47ffd86e000604b38a
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    download_fetch_spacex_last_launch(launch_id, url)