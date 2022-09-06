import os
import requests


from pathlib import Path, PurePath
from file_download import download_image
from dotenv import load_dotenv



def nasa_epic():
  load_dotenv()
  epic_all_url = "https://api.nasa.gov/EPIC/api/natural/all"
  nasa_token = os.environ['NASA_TOKEN']
  params = {"api_key": nasa_token}
  response = requests.get(epic_all_url, params=params)
  response.raise_for_status()
  dates = response.json()
  for date in dates:
    date_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date['date']}"
    response = requests.get(date_url, params=params)
    response.raise_for_status()
    images = response.json()[:10]
    for number, image in enumerate(images):
      image = image["image"]
      date_for_url = date["date"].replace("-", "/")
      file_url = f"https://api.nasa.gov/EPIC/archive/natural/{date_for_url}/png/{image}.png"
      filename = f"epic_nasa_{number}.png"
      Path("images/").mkdir(parents=True, exist_ok=True)
      path = PurePath("images", filename)
      download_image(path, file_url, params)


if __name__ == "__main__":
  nasa_epic()