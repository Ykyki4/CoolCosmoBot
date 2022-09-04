import requests
import os

from pathlib import Path
from file_download import file_download
from file_extension import file_extension
from dotenv import load_dotenv
load_dotenv()

nasa_url = "https://api.nasa.gov/planetary/apod"
nasa_token = os.environ['NASA_TOKEN']

def nasa_picture_day(nasa_url, nasa_token):
  params = {"api_key": nasa_token,
            "count": "30"}
  response = requests.get(nasa_url, params=params)
  response.raise_for_status()
  for n, file_url in enumerate(response.json()):
        params = None
        file_url = file_url.get('url')
        filename = f"nasa_apod_{n}{file_extension(file_url)}"
        Path('images/').mkdir(parents=True, exist_ok=True)
        path = f'images/{filename}'
        file_download(path, file_url, params)

nasa_picture_day(nasa_url, nasa_token)