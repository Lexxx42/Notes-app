"""
\nThis module operates UI of the app.
\nAvailable methods:
\nmain_menu() - main menu UI.
\nchoose_option() - selection of operaton UI.
\nask_about_filename() - filename input UI.
\nselect_id_ui() - id selection UI.
\nask_for_title() - asking for note title UI.
\nask_about_data() - asking for note data UI.
\nnote_added_ui() - add note notificaton UI.
"""

import sys
from .validator import validation_mode, validation_operation, validation_filename, validation_id, validation_data

MAX_SYMBOLS_TITLE = 25
MAX_SYMBOLS_DATA = 50


def main_menu() -> None | tuple[int, int]:
    """ This function is for main menu interface. """
    print("""Notes app. Manage your notes in single place.


Working with:
1 - read notes from a file
2 - add new note
3 - edit note
4 - save notes
5 - delete note

0 - exit
""")

    mode = validation_mode()
    if mode == 0:
        print(f'Note app finished with exit code {mode}')
        sys.exit()
    return choose_option(mode)


def choose_option(main_mode: int) -> None | tuple[int, int]:
    """ This function is for available operations for chosen mode. """
    if main_mode in [1]:
        print("""Options for reading notes
1 - print all notes to the console
2 - print all notes filtered by date
3 - print selected note to the console

0 - previous menu
""")
    operation = validation_operation(main_mode)
    if operation in [10]:
        return main_menu()
    return main_mode, operation


def ask_about_filename() -> str:
    """ This function is for UI for filename input. """
    print("""Enter the filename.

Please enter name of the file without extension,
or press enter to use default filename: notes

Only numbers and letters are allowed.
Extension of the file must be .json
""")
    return validation_filename()


def select_id_ui(data: dict) -> int:
    """ This function is for id selection UI. """
    print("""Please enter id of the note you want to select.
Available ids are presented in the table above.
""")
    return validation_id(data)


def ask_for_title() -> str:
    """ This function is for title getting from user. """
    print(f"""What title do you want for your note?
Maximum number of symbols is {MAX_SYMBOLS_TITLE}
""")
    return validation_data(MAX_SYMBOLS_TITLE)


def ask_about_data() -> str:
    """ This function is for data getting from user. """
    print(f"""Type something to your note
Maximum number of symbols is {MAX_SYMBOLS_DATA}
""")
    return validation_data(MAX_SYMBOLS_DATA)


def note_added_ui() -> None:
    """ This function is for notification about adding a note. """
    print('New note added!')


def ask_about_filename_for_read() -> str:
    """ This function is for UI for filename for reading data. """
    print("""Enter the filename for reading data.

Please enter name of the file without extension,
or press enter to use default filename: notes

Only numbers and letters are allowed.
Extension of the file must be .json
""")
    return validation_filename()


def ask_about_filename_for_save() -> str:
    """ This function is for UI for filename for saving data. """
    print("""Enter the filename for saving data.

Please enter name of the file without extension,
or press enter to use default filename: notes

Only numbers and letters are allowed.
Extension of the file must be .json
""")
    return validation_filename()

def data_saved(srs: str) -> None:
    """ This function is for UI for telling user that data is saved. """
    print(f"""Data saved.
You'll find the data in the following source:
{srs}
""")