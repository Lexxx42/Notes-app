"""
This module uses the PrettyTable library to print notes to the console.
\nAvailable methods:
\npt_print_all() - prints all notes.
\npt_print_filter_date() - prints all notes filtered by date (DESC order).
\npt_print_id_date() - prints note id's and last modified date.
\npt_print_id_selection() - prints note with specific id.
"""

from datetime import datetime
from prettytable import PrettyTable
from .logger import logging

SORTED_PRINT_TIP = 'Sorted by date notes printed as table in console.'
NO_VALID_FILE = 'No valid file for reading.'


def pt_print_all(data_notes: dict) -> None:
    """ Print all notes to the console. """
    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())
        for item in data_notes['notes']:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info('Notes printed as table in console.')
    except TypeError as error:
        print(error)
        logging.exception(error)
    except KeyError as err:
        print(NO_VALID_FILE)
        logging.exception(err)


def pt_print_filter_date(data_notes: dict) -> None:
    """ Print all notes to the console sorted by date (DECS order). """
    try:
        sorted_notes = sorted(data_notes['notes'], key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True)
        table = PrettyTable()
        table.field_names = list(sorted_notes[0].keys())
        for item in sorted_notes:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)


def pt_print_id_date(data_notes: dict) -> None:
    """ Print all note id's and last edited date to the console. """
    try:
        sorted_notes = sorted(data_notes['notes'], key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'), reverse=True)
        table = PrettyTable()
        all_fields = list(sorted_notes[0].keys())
        table.field_names = [_ for _ in all_fields if _ in ['id', 'date']]

        for item in sorted_notes:
            table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
    except IndexError as index_err:
        print('Nothing to delete!')
        logging.exception(index_err)
        return -1


def pt_print_id_selection(data_notes: dict, idx: int) -> None:
    """ Print note with specific id to the console. """
    try:
        table = PrettyTable()
        table.field_names = list(data_notes['notes'][0].keys())

        for item in data_notes['notes']:
            if item.get('id') == idx:
                table.add_row([item[i] for i in table.field_names])

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
    except KeyError as error:
        print(NO_VALID_FILE)
        logging.exception(error)
