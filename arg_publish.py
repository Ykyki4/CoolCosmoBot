import os
import random
import telegram
import argparse
from pathlib import PurePath
from dotenv import load_dotenv



def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    args = parser.parse_args()
    return args


def arg_publish():

    try:
        image_path = PurePath('images', arg_parser().image_path)
        with open(image_path, 'rb') as file:
            bot.send_document(chat_id=chat_id, document=file)

    except:
        images = os.walk('images')
        for image_list in images:
            random_image = random.choice(image_list[2])
            image_path = PurePath('images', random_image)
            with open(image_path, 'rb') as file:
                bot.send_document(chat_id=chat_id, document=file)


if __name__ == "__main__":
    load_dotenv()
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    bot = telegram.Bot(token=telegram_token)
    arg_publish()