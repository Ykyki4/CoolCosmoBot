import os
import random
import time
import telegram
from pathlib import PurePath
from dotenv import load_dotenv


def while_publish():
  while True:
    images_path = os.walk('images')
    for i, j, images in images_path:
      random.shuffle(images)
      for image in images:
        image_path = PurePath('images', image)
        with open(image_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)
        images.remove(image)
        publish_delay = os.environ['PUBLISH_DELAY']
        time.sleep(float(publish_delay))


def main():
  while_publish()


if __name__ == "__main__":
  load_dotenv()
  telegram_token = os.environ['TELEGRAM_TOKEN']
  chat_id = os.environ['CHAT_ID']
  bot = telegram.Bot(token=telegram_token)
  main()