import json
from prettytable import PrettyTable

DEFAULT_DIRNAME = '../Data_store/'
DEFAULT_FILENAME = 'notes.json'


def load_from_file(filename):
    with open(filename, encoding='utf-8') as file:
        data = json.load(file)
    return data


data = load_from_file(DEFAULT_DIRNAME + DEFAULT_FILENAME)

x = PrettyTable()
x.field_names = list(data["notes"][0].keys())
for item in data["notes"]:
    x.add_row([item[i] for i in x.field_names])

print(x)