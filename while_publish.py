import os
import random
import time
import telegram
from dotenv import load_dotenv

load_dotenv()
telegram_token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_token)
def while_publish():
  while True:
    images = os.walk('images')
    for image_list in images:
      random.shuffle(image_list[2])
      for image in image_list[2]:
        bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
        image_list[2].remove(image)
        publish_delay = os.environ['PUBLISH_DELAY']
        time.sleep(float(publish_delay))

while_publish()