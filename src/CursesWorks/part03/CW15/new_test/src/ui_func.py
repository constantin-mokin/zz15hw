from exceptions import WrongInputError
from config import (
    EXIT,
    CONFIG,
)


def print_divider():
    print('*' * 10)


def start_message():
    print_divider()
    print('start')
    print_divider()


def finish_message():
    print_divider()
    print('See you later')
    print_divider()


def input_arguments():
    a = int(input('Input the first argument: '))
    b = int(input('Input the second argument: '))
    return a, b


def wait_for_enter():
    print_divider()
    input('PRESS ENTER TO CONTINUE')
    print_divider()


def call_func(func):
    a, b = input_arguments()
    result = func(a, b)
    return a, b, result


def print_exit_choice():
    print_divider()
    print(f'{EXIT}. EXIT')
    print_divider()


def print_choices():
    print('Choose operation:')
    operations = CONFIG['operations']
    available_operations = sorted(CONFIG['available_operations'])
    list(map(lambda operation_code: print(operations[operation_code]['choice_message']), available_operations))


def choose_operation():
    print_choices()
    choice = int(input('Input your choice: '))
    if not choice:
        return EXIT
    operation_data = CONFIG['operations'].get(choice)

    if not operation_data:
        raise WrongInputError
    a, b, result = call_func(operation_data['operation'])
    print(operation_data['result_pattern'].format(a, b, result))
    wait_for_enter()


def ui():
    start_message()
    while True:
        try:
            result = choose_operation()
            if result == EXIT:
                break
        except Exception as err:
            print(err)
            wait_for_enter()
        print_divider()