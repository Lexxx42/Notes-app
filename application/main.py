from .logger import logging
from .user_interface import main_menu, ask_about_filename
from .file_worker import write_to_file, load_from_file
from .data_checker_and_filler import check_data_storage, generate_filename, DEFAULT_SRC
from .pretty_print import pt_print_all, pt_print_filter_date


def entrance_point() -> None:
    logging.info('Start program.')
    check_data_storage()
    operation_type, operation_code = main_menu()
    logging.info(f'operation chosen = {operation_type}, operation code = {operation_code}')
    main_handler(operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()


def main_handler(operation_code: int) -> None:
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


def wait_for_continue() -> None:
    if input("Press Any key to continue: "):
        return
