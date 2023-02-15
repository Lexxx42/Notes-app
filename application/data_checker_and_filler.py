from os import path, makedirs
from .logger import logging
from .file_worker import write_to_file

DEFAULT_DIRNAME = './Data_store/'
DEFAULT_FILENAME = 'notes.json'
DEFAULT_EXTENSION = '.json'
DEFAULT_SRC = DEFAULT_DIRNAME + DEFAULT_FILENAME
TEST_DATA_JSON = {"notes": [
    {"id": 1, "title": "Buy milk", "data": "I need to buy some coconut milk for my coffee.", "date": "03-02-2023"},
    {"id": 2, "title": "Call teacher", "data": "Ask about mistakes found in my homework.", "date": "09-02-2023"},
    {"id": 8, "title": "Ask Mark about his life", "data": "I should call my old friend Mark this friday.",
     "date": "13-02-2023"},
    {"id": 12, "title": "Use time machine", "data": "Use time machine to travel back to the past.",
     "date": "01-01-1990"}]}


def check_data_storage() -> None:
    logging.info('Checking data.')
    check_folder()
    check_notes_json()
    logging.info('Data checked.')


def check_folder() -> None:
    try:
        if not path.exists(DEFAULT_DIRNAME):
            makedirs(DEFAULT_DIRNAME)
            logging.info(f'Folder {DEFAULT_DIRNAME} created for data storage.')
    except OSError as error:
        print(f'cannot create {DEFAULT_DIRNAME} directory', error)
        logging.exception(f'cannot create {DEFAULT_DIRNAME} directory', error)


def check_notes_json() -> None:
    try:
        if not path.exists(DEFAULT_SRC):
            fill_notes()
            logging.info(f'Notes {DEFAULT_FILENAME} file created in data strage {DEFAULT_DIRNAME}.')
    except OSError as error:
        print(f'cannot create {DEFAULT_FILENAME} file', error)
        logging.exception(f'cannot create {DEFAULT_FILENAME} file', error)


def fill_notes() -> None:  # TODO: need try.
    write_to_file(TEST_DATA_JSON, DEFAULT_SRC)
    logging.info(f'Notes filled in file {DEFAULT_FILENAME}.')


def generate_filename(custom_filename: str) -> str:
    try:
        custom_src = DEFAULT_DIRNAME + custom_filename + DEFAULT_EXTENSION
    except Exception as e:
        print(e)
        logging.exception(e)
    return custom_src
