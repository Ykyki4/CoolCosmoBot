import os
import random
import telegram
import argparse
from dotenv import load_dotenv


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    return args

load_dotenv()
telegram_token = os.environ['TELEGRAM_TOKEN']
chat_id = os.environ['CHAT_ID']
bot = telegram.Bot(token=telegram_token)
def arg_publish():
    try:
        file_path = arg_parser().file_path
        bot.send_document(chat_id=chat_id, document=open(f'images/{file_path}', 'rb'))
    except:
        images = os.walk('images')
        for image_list in images:
            image = random.choice(image_list[2])
            bot.send_document(chat_id=chat_id, document=open(f'images/{image}', 'rb'))
arg_publish()
