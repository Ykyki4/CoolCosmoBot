import os
import requests


from pathlib import Path
from file_download import download_image
from dotenv import load_dotenv



def nasa_epic():

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
      download_image(path, file_url, params)


def main():
  nasa_epic()


if __name__ == "__main__":
  epic_all_url = "https://api.nasa.gov/EPIC/api/natural/all"
  nasa_token = os.environ['NASA_TOKEN']
  load_dotenv()
  main()