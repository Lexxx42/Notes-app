from os import path, makedirs
from .logger import logging
from .user_interface import main_menu
from .file_worker import write_file

DEFAULT_DIRNAME = './Data_store/'
DEFAULT_FILENAME = 'notes.json'
TEST_DATA_JSON = '{ "notes": [ { "id": "1", "title": "Buy milk",' \
                 '"data": "I need to buy some coconut milk for my coffee.",' \
                 '"date": "03-02-2023" }, { "id": "2", "title": "Call teacher",' \
                 '"data": "Ask about mistakes found in my homework.",' \
                 '"date": "09-02-2023" }, { "id": "8", "title": "Ask Mark about his life",' \
                 '"data": "I should call my old friend Mark this friday.",' \
                 '"date": "13-02-2023" } ] }'


def entrance_point():
    logging.info('Start program.')
    check_data()
    operation_type, operation_code = main_menu()
    logging.info(f'operation chosen = {operation_type}, operation code = {operation_code}')
    # options(operation_type, operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()


def check_data():
    check_folder()
    check_notes()


def check_folder():
    try:
        if not path.exists(DEFAULT_DIRNAME):
            makedirs(DEFAULT_DIRNAME)
    except OSError as error:
        print(f'cannot create {DEFAULT_DIRNAME} directory', error)
        logging.ERROR(f'cannot create {DEFAULT_DIRNAME} directory', error)


def check_notes():
    try:
        if not path.exists(DEFAULT_DIRNAME + DEFAULT_FILENAME):
            fill_notes()
    except OSError as error:
        print(f'cannot create {DEFAULT_FILENAME} file', error)
        logging.ERROR(f'cannot create {DEFAULT_FILENAME} file', error)


def fill_notes():
    write_file(TEST_DATA_JSON)
