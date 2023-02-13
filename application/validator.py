from .logger import logging

AVAILABLE_MODES_MAIN_MENU = 6
MUST_BE_INTEGER = 'Incorrect input! Input must be an integer.'
INCORRECT_INPUT = 'Incorrect input! Please look at the available modes.'


def validation_mode() -> int:
    """ Function for check user's input from main mode.
    \nChecks user input and returns main menu mode.
    """
    while True:
        try:
            main_menu_mode = int(input('Which mode do you need: '))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if main_menu_mode in range(AVAILABLE_MODES_MAIN_MENU):
            if main_menu_mode == 0:
                logging.info('Finished work from main menu.')
            else:
                logging.info(f'Main mode of interface = {main_menu_mode}')
            return main_menu_mode
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)


def validation_operation(main_menu_mode) -> int:
    """ Function for check user's input for operation mode.
    \nChecks user input and returns operation mode."""
    match main_menu_mode:
        case 1:
            validate_read()


def validate_read():
    number_of_available_modes = 4
    while True:
        try:
            operation_type = int(input("Enter operation code: "))
        except ValueError:
            print(MUST_BE_INTEGER)
            logging.exception(MUST_BE_INTEGER)
            continue
        if operation_type in range(number_of_available_modes):
            logging.info(f'operation code for read = {operation_type}')
            return 10 + operation_type
        print(INCORRECT_INPUT)
        logging.exception(INCORRECT_INPUT)
