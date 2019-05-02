from func import calc_diff, calc_div, calc_mult, calc_sum

def test_calc_sum():
    result = calc_sum(1, 2)
    if result == 3:
        print('test ok')
    else:
        print('test failed')

# i tak dalee po ostalnim funkciam kalkulyatora