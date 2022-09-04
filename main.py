# import requests
import os
# import datetime
#
# from pathlib import Path
# from nasa_apod import nasa_picture_day
# from fetch_spacex_last_launch import fetch_spacex_last_launch
# from nasa_epic import nasa_epic
import random
import time
import telegram
from dotenv import load_dotenv




if __name__ == "__main__":
  load_dotenv()
  telegram_token = "5656387036:AAHwrd28ThB1YOwM4jHqAom8LgnCgo8svXA"
  chat_id = "-1001617192356"
  bot = telegram.Bot(token=telegram_token)
  while True:
    images = os.walk('images')
    for image_list in images:
      random.shuffle(image_list[2])
      for image in image_list[2]:
        bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
        image_list[2].remove(image)
        print(image_list[2])
        publish_delay = os.environ['PUBLISH_DELAY']
        time.sleep(float(publish_delay))





