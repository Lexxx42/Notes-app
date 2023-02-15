import json
from .logger import logging


def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file_json:
        json.dump(data, file_json, ensure_ascii=False)
    logging.info(f'Write data to {filename}')


def load_from_file(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'Read data from {filename}')
        return data
    except OSError as e:
        print(e)
        logging.exception(e)
