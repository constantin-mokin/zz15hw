from func import (
    calc_sum,
    calc_diff,
    calc_mult,
    calc_div,
)

EXIT = 0
SUM = 1
DIFF = 2
MULT = 3
DIV = 4

CONFIG = {
    'operations': {
        SUM: {
            'operation': calc_sum,
            'choice_message': f'{SUM}. Calc sum',
            'result_pattern': '{} + {} = {}',
        },
        DIFF: {
            'operation': calc_diff,
            'choice_message': f'{DIFF}. Calc diff',
            'result_pattern': '{} - {} = {}',
        },
        MULT: {
            'operation': calc_mult,
            'choice_message': f'{MULT}. Calc mult',
            'result_pattern': '{} * {} = {}',
        },
        DIV: {
            'operation': calc_div,
            'choice_message': f'{DIV}. Calc div',
            'result_pattern': '{} / {} = {}',
        },
    },
    'available_operations': [
        SUM,
        DIFF,
        MULT,
        DIV,
    ],
}