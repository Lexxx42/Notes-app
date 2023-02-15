from prettytable import PrettyTable
from .logger import logging


def prettytable_print_all(data_notes):
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

def prettytable_print_filter_date(data_notes):
    print("desc date")