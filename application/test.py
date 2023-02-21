import json
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
        x.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        print(x)
    except TypeError as e:
        print(e)


def prettytable_print_sorted(data_notes):
    try:
        x = PrettyTable()
        x.field_names = list(data_notes["notes"][0].keys())
        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        x.sortby = "date"
        x.reversesort = True
        print(x)
    except TypeError as e:
        print(e)


def pt_print_id_date(data_notes: dict) -> None:
    try:
        x = PrettyTable()
        all_fields = list(data_notes["notes"][0].keys())

        x.field_names = [_ for _ in all_fields if _ in ['id', 'date']]

        for item in data_notes["notes"]:
            x.add_row([item[i] for i in x.field_names])
        x.sortby = "date"
        x.reversesort = True
        print(x)
    except TypeError as e:
        print(e)


data = load_from_file(DEFAULT_DIRNAME + DEFAULT_FILENAME)
pt_print_id_date(data)
