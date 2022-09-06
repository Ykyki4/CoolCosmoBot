import requests
import os

from pathlib import Path
from file_download import download_image
from file_extension import file_extension
from dotenv import load_dotenv


def nasa_picture_day():
    params = {"api_key": nasa_token,
                "count": "30"}
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    for n, image_url in enumerate(response.json()):
            params = None
            image_url = image_url.get('url')
            filename = f"nasa_apod_{n}{file_extension(image_url)}"
            Path('images/').mkdir(parents=True, exist_ok=True)
            path = f'images/{filename}'
            download_image(path, image_url, params)


if __name__ == "__main__":
    nasa_token = os.environ['NASA_TOKEN']
    nasa_url = "https://api.nasa.gov/planetary/apod"
    load_dotenv()
    nasa_picture_day()