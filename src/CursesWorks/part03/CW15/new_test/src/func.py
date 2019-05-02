def calc_sum(a, b):
    return a + b


def calc_diff(a, b):
    return a - b


def calc_mult(a, b):
    return a * b


def calc_div(a, b):
    if not b:
        raise ZeroDivisionError('AAAA')
    return a / b