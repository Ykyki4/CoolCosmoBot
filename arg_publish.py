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


def publish_arg():
    load_dotenv()
    bot = telegram.Bot(token=telegram_token)
    image_path = arg_parser().image_path
    if image_path:
        image_path = PurePath('images', image_path)
        publish_image(image_path, chat_id, bot)
    else:
        dir_images = os.walk('images')
        for i, j, images in dir_images:
            random_image = random.choice(images)
            image_path = PurePath('images', random_image)
            publish_image(image_path, chat_id, bot)


if __name__ == "__main__":
    telegram_token = os.environ['TELEGRAM_TOKEN']
    chat_id = os.environ['CHAT_ID']
    publish_arg()