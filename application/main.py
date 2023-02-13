from .logger import logging

def entrance_point():
    logging.info('Start program.')
    operation_type, operation_code = main_menu()
    logging.info(f'operation chosen = {operation_type}, operation code = {operation_code}')
    # options(operation_type, operation_code)
    logging.info('Session finish')
    if operation_type != 0:
        entrance_point()

def main_menu():
    return (0, 2)

