import os
import random
import telegram
import argparse
from pathlib import PurePath
from dotenv import load_dotenv
from publish_image import publish_image



def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", nargs="?")
    args = parser.parse_args()
    return args


def arg_publish():
    load_dotenv()
    bot = telegram.Bot(token=telegram_token)
    if arg_parser().image_path:
        image_path = PurePath('images', arg_parser().image_path)
        publish_image(image_path, chat_id, bot)
    else:
        dir_images = os.walk('images')
        for images in dir_images:
            random_image = random.choice(images[2])
            image_path = PurePath('images', random_image)
            publish_image(image_path, chat_id, bot)


if __name__ == "__main__":
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    arg_publish()