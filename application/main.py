"""
\nThis module operates all functions for the app.
\nAvailable methods:
\nentrance_point() - main loop of the program.
\nmain_handler() - handles different handlers for operations available.
\nhandler_for_read() - handles different operations for read mode.
\nwait_for_continue() - waiting user to continue.
\nhandler_for_add() - adding new note to the file.
\nhandler_for_save() - saving note data to the file.
\nhandler_for_edit() - editing note data in the file.
"""

from datetime import datetime
from .logger import logging
from .user_interface import main_menu, ask_about_filename, select_id_ui, ask_for_title, ask_about_data, note_added_ui, \
    ask_about_filename_for_read, ask_about_filename_for_save, data_saved, ask_about_data_edit
from .file_worker import write_to_file, load_from_file
from .data_checker_and_filler import check_data_storage, generate_filesource, DEFAULT_SRC, fill_new_note
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
        handler_for_add()
    elif str(operation_code)[0] in ('3'):
        handler_for_edit()
    elif str(operation_code)[0] in ('4'):
        handler_for_save()


def handler_for_read(operation_code: int) -> None:
    """ Function for selection of operations for read mode. """
    match operation_code:
        case 11:
            file_name_valid = ask_about_filename()
            print(file_name_valid)
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))
            pt_print_all(data_from_file)
            wait_for_continue()
        case 12:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))
            pt_print_filter_date(data_from_file)
            wait_for_continue()
        case 13:
            file_name_valid = ask_about_filename()
            if not file_name_valid:
                data_from_file = load_from_file(DEFAULT_SRC)
            else:
                data_from_file = load_from_file(generate_filesource(file_name_valid))
            pt_print_id_date(data_from_file)
            pt_print_id_selection(data_from_file, select_id_ui(data_from_file))
            wait_for_continue()


def handler_for_add() -> None:
    """ Function for add note operations. """
    file_name_valid = ask_about_filename()
    if not file_name_valid:
        source = DEFAULT_SRC
        data_from_file = load_from_file(source)
    else:
        source = generate_filesource(file_name_valid)
        data_from_file = load_from_file(source)
    try:
        note_id = data_from_file['notes'][-1]['id'] + 1
    except Exception as err:
        print(err)
        return -1
        logging.exception(err)
    finally:
        wait_for_continue()
    note_title = ask_for_title()
    note_data = ask_about_data()
    date = datetime.today().strftime('%d-%m-%Y')
    upd_data = fill_new_note(data_from_file, note_id, note_title, note_data, date)
    write_to_file(upd_data, source)
    note_added_ui()
    wait_for_continue()


def handler_for_save() -> None:
    """ Function for save note file operations. """
    file_name_valid = ask_about_filename_for_read()
    try:
        if not file_name_valid:
            source = DEFAULT_SRC
            data_from_file = load_from_file(source)
        else:
            source = generate_filesource(file_name_valid)
            data_from_file = load_from_file(source)
    except Exception as err:
        print(err)
        return -1
        logging.exception(err)
    finally:
        wait_for_continue()
    filename_for_save = ask_about_filename_for_save()
    if not filename_for_save:
        source = DEFAULT_SRC
    else:
        source = generate_filesource(filename_for_save)
    write_to_file(data_from_file, source)
    data_saved(source)
    logging.info(f'Data saved to {source=}')
    wait_for_continue()


def handler_for_edit() -> None:
    """ Function for editing notes in the file operations. """
    file_name_valid = ask_about_filename_for_read()
    try:
        if not file_name_valid:
            source = DEFAULT_SRC
            data_from_file = load_from_file(source)
        else:
            source = generate_filesource(file_name_valid)
            data_from_file = load_from_file(source)
    except Exception as err:
        print(err)
        return -1
        logging.exception(err)
    finally:
        wait_for_continue()

    pt_print_id_date(data_from_file)
    pt_print_id_selection(data_from_file, select_id_ui(data_from_file))
    wait_for_continue()
    ask_about_data_edit()

    exit()
    write_to_file(data_from_file, source)
    data_saved(source)
    logging.info(f'Data saved to {source=}')
    wait_for_continue()


def wait_for_continue() -> None:
    """ Function to wait for user to continue. """
    if input('Press any key to continue: '):
        return
