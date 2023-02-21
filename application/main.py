"""
\nThis module operates all functions for the app.
\nAvailable methods:
\nentrance_point() - main loop of the program.
\nmain_handler() - handles different handlers for operations available.
\nhandler_for_read() - handles different operations for read mode.
\nwait_for_continue() - waiting user to continue.
\nhandler_for_add() - adding new note to the file.
"""

from .logger import logging
from .user_interface import main_menu, ask_about_filename, select_id_ui
from .file_worker import write_to_file, load_from_file
from .data_checker_and_filler import check_data_storage, generate_filename, DEFAULT_SRC
from .pretty_print import pt_print_all, pt_print_filter_date, pt_print_id_date, \
    pt_print_id_selection


def entrance_point() -> None:
    """ Function for main sequence of the program.
    \nIn loop until user selects exit from main menu. """
    logging.info('Start program.')
    check_data_storage()
    operation_type, operation_code = main_menu()
    logging.info(f'Operation chosen = {operation_type}, operation code = {operation_code}')
    main_handler(operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()


def main_handler(operation_code: int) -> None:
    """ Function for selecting handler for operation. """
    if str(operation_code)[0] in ('1'):
        handler_for_read(operation_code)
    elif str(operation_code)[0] in ('2'):
        handler_for_add(operation_code)


def handler_for_read(operation_code: int) -> None:
    """ Function for selection of operations for read mode. """
    match operation_code:
        case 11:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filename(file_name_valid))
            pt_print_all(data_from_file)
            wait_for_continue()
        case 12:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filename(file_name_valid))
            pt_print_filter_date(data_from_file)
            wait_for_continue()
        case 13:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filename(file_name_valid))
            pt_print_id_date(data_from_file)
            pt_print_id_selection(data_from_file, select_id_ui(data_from_file))
            wait_for_continue()


def handler_for_add(operation_code: int) -> None:
    """ Function for add note operations. """
    file_name_valid = ask_about_filename()
    if not file_name_valid:
        data_from_file = load_from_file(DEFAULT_SRC)
    else:
        data_from_file = load_from_file(generate_filename(file_name_valid))
    add_note(data_from_file)
    note_id = next_id = data['notes'][-1]['id']
    note_title = ask_for_title()
    note_data = ask_about_data()
    date = date!
    wait_for_continue()

    def wait_for_continue() -> None:
        """ Function to wait for user to continue. """
        if input("Press Any key to continue: "):
            return
