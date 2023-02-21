"""
\nThis module operates all functions checking files and filling data.
\nAvailable methods:
\ncheck_data_storage() - check for folder and file for notes.
\ncheck_folder() - checking existance of folder for notes.
\ncheck_notes_json() - checking existance of file for notes.
\nfill_notes() - filling test note data.
\nfill_new_note() - adds new note to the data.
\nfill_dict() - combines set of data to the note.
"""

from os import path, makedirs
from typing import Any
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
    """ This function is for checking data storage. """
    logging.info('Checking data.')
    check_folder()
    check_notes_json()
    logging.info('Data checked.')


def check_folder() -> None:
    """ This function is for checking existance of folder for notes. """
    try:
        if not path.exists(DEFAULT_DIRNAME):
            makedirs(DEFAULT_DIRNAME)
            logging.info(f'Folder {DEFAULT_DIRNAME} created for data storage.')
    except OSError as error:
        print(f'cannot create {DEFAULT_DIRNAME} directory', error)
        logging.exception(f'cannot create {DEFAULT_DIRNAME} directory', error)


def check_notes_json() -> None:
    """ This function is for checking existance of file for notes. """
    try:
        if not path.exists(DEFAULT_SRC):
            fill_notes()
            logging.info(f'Notes {DEFAULT_FILENAME} file created in data strage {DEFAULT_DIRNAME}.')
    except OSError as error:
        print(f'Cannot create {DEFAULT_FILENAME} file', error)
        logging.exception(f'Cannot create {DEFAULT_FILENAME} file', error)


def fill_notes() -> None:
    """ This function is for filling notes for test data. """
    try:
        write_to_file(TEST_DATA_JSON, DEFAULT_SRC)
    except Exception as fillerr:
        print(fillerr)
        logging.exception(fillerr)
    logging.info(f'Notes filled in file {DEFAULT_FILENAME}.')


def generate_filesourse(custom_filename: str) -> str:
    """ This functions is for generation of sourse to the note file. """
    try:
        custom_src = DEFAULT_DIRNAME + custom_filename + DEFAULT_EXTENSION
    except Exception as err:
        print(err)
        logging.exception(err)
    return custom_src


def fill_new_note(data: dict, note_id: int,
                  note_title: str, note_data: str, date: str) -> dict:
    """ This functions fills data for a new note. """
    new_note = fill_dict(('id', note_id), ('title', note_title), ('data', note_data), ('date', date))
    data['notes'].append(new_note)
    return data


def fill_dict(*args: Any) -> dict:
    """ This function creates new note as a dictionary. """
    return {arg[0]: arg[1] for arg in args}

