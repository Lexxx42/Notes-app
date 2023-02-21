"""Test."""
import json
import time
from prettytable import PrettyTable

DEFAULT_DIRNAME = '../Data_store/'
DEFAULT_FILENAME = 'notes.json'


def load_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data


def prettytable_print_all(data_notes):
    try:
        x = PrettyTable()
        x.field_names = list(data_notes['notes'][0].keys())
        for item in data_notes['notes']:
            x.add_row([item[i] for i in x.field_names])
        print(x)
    except TypeError as e:
        print(e)


def prettytable_print_sorted(data_notes):
    try:
        x = PrettyTable()
        x.field_names = list(data_notes['notes'][0].keys())
        for item in data_notes['notes']:
            x.add_row([item[i] for i in x.field_names])
        x.sortby = 'date'
        x.reversesort = True
        print(x)
    except TypeError as e:
        print(e)


def pt_print_id_date(data_notes: dict) -> None:
    try:
        x = PrettyTable()
        all_fields = list(data_notes['notes'][0].keys())

        x.field_names = [_ for _ in all_fields if _ in ['id', 'date']]
        [x.add_row([item[i] for i in x.field_names]) for item in data_notes['notes']]

        x.sortby = 'date'
        x.reversesort = True
        print(x)
    except TypeError as e:
        print(e)


data = load_from_file(DEFAULT_DIRNAME + DEFAULT_FILENAME)

idx = [data['notes'][i]['id'] for i in range(len(data['notes']))]


# pt_print_id_date(data)


def pt_print_id_selection(data_notes: dict, idx: int) -> None:
    """ Print note with specific id to the console. """
    try:
        x = PrettyTable()
        x.field_names = list(data_notes["notes"][0].keys())

        [x.add_row([item[i] for i in x.field_names]
                   ) for item in data_notes['notes'] if item.get('id') == idx]
        print(x)

    except TypeError as e:
        print(e)


# pt_print_id_selection(data, 12)


def test(data, idx):
    for i in range(4):
        if data['notes'][i].get('id') == idx:
            print('+')
        else:
            print('-')


next_id = data['notes'][-1]['id']
# print(next_id)

from datetime import datetime


# print(datetime.today().strftime('%d-%m-%Y'))

# print(len("I need to buy some coconut milk for my coffee."))


def fill_new_note(sourse: str, data: dict, note_id: int,
                  note_title: str, note_data: str, date: str) -> tuple[dict, str]:
    """ This functions fills data for a new note. """
    new_note = fill_dict(('id', note_id), ('title', note_title), ('data', note_data), ('date', date))
    return new_note


def fill_dict(*args) -> dict:
    """ This function creates new note as a dictionary. """
    return {arg[0]: arg[1] for arg in args}
