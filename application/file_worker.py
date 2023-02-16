import json
from .logger import logging


def write_to_file(data: dict, filename: str) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as file_json:
            json.dump(data, file_json, ensure_ascii=False)
        logging.info(f'Write data to {filename}')
    except FileNotFoundError as err:
        print(f'File {filename} not found.  Aborting')
        logging.exception(err)
    except OSError as err:
        print(f'OS error occurred trying to open {filename}')
        logging.exception(err)
    except Exception as err:
        print(f'Unexpected error opening {filename} is', repr(err))
        logging.exception(err)


def load_from_file(filename: str) -> dict:
    try:
        with open(filename, encoding='utf-8') as file:
            data = json.load(file)
        logging.info(f'Read data from {filename}')
        return data
    except FileNotFoundError as err:
        print(f'File {filename} not found.  Aborting')
        logging.exception(err)
    except OSError:
        print(f'OS error occurred trying to open {filename}')
        logging.exception(err)
    except Exception as err:
        print(f'Unexpected error opening {filename} is', repr(err))
        logging.exception(err)
    except json.decoder.JSONDecodeError as e:
        print(e)
        logging.exception(e)
