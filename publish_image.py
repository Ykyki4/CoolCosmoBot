


def publish_image(image_path, chat_id, bot):
    with open(image_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)