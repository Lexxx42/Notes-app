import sys
from .validator import validation_mode, validation_operation


def main_menu() -> None | tuple[int, int]:
    """ This function is for main menu of prison interface. """
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


def choose_option(main_mode) -> None | tuple[int, int]:
    """ This function is for available operations for chosen mode. """
    match main_mode:
        case 1:
            print("""Options for reading notes
1 - print all notes to the console
2 - print all notes filtered by date
3 - print selected note to the console

0 - previous menu
""")
            operation = validation_operation(main_mode)
    if operation in [10]:
        return main_menu()
    else:
        return main_mode, operation
