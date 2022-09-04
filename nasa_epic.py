import os
import requests

from pathlib import Path
from file_download import file_download
from dotenv import load_dotenv
load_dotenv()

epic_all_url = "https://api.nasa.gov/EPIC/api/natural/all"
nasa_token = os.environ['NASA_TOKEN']


def nasa_epic(epic_all_url, nasa_token):
  params = {"api_key": nasa_token}
  response = requests.get(epic_all_url, params=params)
  response.raise_for_status()
  dates = response.json()
  for date in dates:
    date_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date['date']}"
    response = requests.get(date_url, params=params)
    response.raise_for_status()
    images = response.json()[:10]
    for n, image in enumerate(images):
      image = image['image']
      date_for_url = date['date'].replace("-", "/")
      file_url = f"https://api.nasa.gov/EPIC/archive/natural/{date_for_url}/png/{image}.png"
      filename = f"epic_nasa_{n}.png"
      Path('images/').mkdir(parents=True, exist_ok=True)
      path = f'images/{filename}'
      file_download(path, file_url, params)

nasa_epic(epic_all_url, nasa_token)