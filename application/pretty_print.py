"""
This module uses the PrettyTable library to print notes to the console.
\nAvailable methods:
\npt_print_all() - prints all notes.
\npt_print_filter_date() - prints all notes filtered by date (DESC order).
\npt_print_id_date() - prints note id's and last modified date.
"""

from prettytable import PrettyTable
from .logger import logging


def pt_print_all(data_notes: dict) -> None:
    """ Print all notes to the console. """
    try:
        x = PrettyTable()
        x.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        print(x)
        logging.info('Notes printed as table in console.')
    except TypeError as e:
        print(e)
        logging.exception(e)


def pt_print_filter_date(data_notes: dict) -> None:
    """ Print all notes to the console sorted by date (DECS order). """
    try:
        x = PrettyTable()
        x.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        x.sortby = "date"
        x.reversesort = True
        print(x)
        logging.info('Sorted by date notes printed as table in console.')
    except TypeError as e:
        print(e)
        logging.exception(e)


def pt_print_id_date(data_notes: dict) -> None:
    """ Print all note id's and last edited date to the console. """
    try:
        x = PrettyTable()
        all_fields = list(data_notes["notes"][0].keys())

        x.field_names = [_ for _ in all_fields if _ in ['id', 'date']]

        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        x.sortby = "date"
        x.reversesort = True
        print(x)
        logging.info('Sorted by date notes printed as table in console.')
    except TypeError as e:
        print(e)
        logging.exception(e)
