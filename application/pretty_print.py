"""
This module uses the PrettyTable library to print notes to the console.
\nAvailable methods:
\npt_print_all() - prints all notes.
\npt_print_filter_date() - prints all notes filtered by date (DESC order).
\npt_print_id_date() - prints note id's and last modified date.
\npt_print_id_selection() - prints note with specific id.
"""

from prettytable import PrettyTable
from .logger import logging

SORTED_PRINT_TIP = 'Sorted by date notes printed as table in console.'


def pt_print_all(data_notes: dict) -> None:
    """ Print all notes to the console. """
    try:
        table = PrettyTable()
        table.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            table.add_row([item[i] for i in table.field_names])
        print(table)
        logging.info('Notes printed as table in console.')
    except TypeError as e:
        print(e)
        logging.exception(e)


def pt_print_filter_date(data_notes: dict) -> None:
    """ Print all notes to the console sorted by date (DECS order). """
    try:
        table = PrettyTable()
        table.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            table.add_row([item[i] for i in table.field_names])
        table.sortby = "date"
        table.reversesort = True
        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as e:
        print(e)
        logging.exception(e)


def pt_print_id_date(data_notes: dict) -> None:
    """ Print all note id's and last edited date to the console. """
    try:
        table = PrettyTable()
        all_fields = list(data_notes["notes"][0].keys())
        table.field_names = [_ for _ in all_fields if _ in ['id', 'date']]

        [table.add_row([item[i] for i in table.field_names]) for item in data_notes['notes']]

        table.sortby = "date"
        table.reversesort = True
        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)


def pt_print_id_selection(data_notes: dict, idx: int) -> None:
    """ Print note with specific id to the console. """
    try:
        table = PrettyTable()
        table.field_names = list(data_notes["notes"][0].keys())

        [table.add_row([item[i] for i in table.field_names]
                   ) for item in data_notes['notes'] if item.get('id') == idx]

        print(table)
        logging.info(SORTED_PRINT_TIP)
    except TypeError as err:
        print(err)
        logging.exception(err)
