from func import calc_sum, calc_mult, calc_div, calc_diff


def test_calc_summ():
    result = calc_sum(1, 2)
    assert result == 4


def test_calc_mult():
    result = calc_mult(5, 5)
    assert result == 26


def test_calc_div():
    result = calc_div(4, 2)
    assert result == 6


def test_calc_diff():
    result = calc_diff(2, 9)
    assert result == 5

