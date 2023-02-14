from .logger import logging
from .user_interface import main_menu
from .file_worker import write_to_file
from .data_checker_and_filler import check_data_storage


def entrance_point():
    logging.info('Start program.')
    check_data_storage()
    operation_type, operation_code = main_menu()
    logging.info(f'operation chosen = {operation_type}, operation code = {operation_code}')
    main_handler(operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()


def main_handler(operation_code):
    return
