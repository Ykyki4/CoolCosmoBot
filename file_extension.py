import os


def file_extension(file_url):
    splited_url = os.path.splitext(file_url)
    if splited_url[1] == '.jpg' or '.png' or '.gif':
      return splited_url[1]
    else:
      return None