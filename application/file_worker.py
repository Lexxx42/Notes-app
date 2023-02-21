"""
\nThis module operates work with files.
\nAvailable methods:
\nwrite_to_file() - writing memory to the file.
\nload_from_file() - loading data from file to the memory.
"""

import json
from .logger import logging


def write_to_file(data: dict, sourse: str) -> None:
    """ This function is for writing data to the file. """
    try:
        with open(sourse, 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, ensure_ascii=False)
        logging.info(f'Write data to {sourse}')
    except FileNotFoundError as err:
        print(f'Sourse {sourse} not found. Aborting')
        logging.exception(err)
    except OSError as err:
        print(f'OS error occurred trying to open {sourse}')
        logging.exception(err)
    except Exception as error:
        print(f'Unexpected error opening {sourse} is', repr(error))
        logging.exception(error)


def load_from_file(sourse: str) -> dict:
    """ This function is for loading data from the file. """
    try:
        with open(sourse, encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'Read data from {sourse}')
        return data
    except FileNotFoundError as err:
        print(f'Sourse {sourse} not found. Aborting')
        logging.exception(err)
    except OSError as oserr:
        print(f'OS error occurred trying to open {sourse}')
        logging.exception(oserr)
    except Exception as excerr:
        print(f'Unexpected error opening {sourse} is', repr(excerr))
        logging.exception(excerr)
    except json.decoder.JSONDecodeError as jsonerr:
        print(jsonerr)
        logging.exception(jsonerr)
