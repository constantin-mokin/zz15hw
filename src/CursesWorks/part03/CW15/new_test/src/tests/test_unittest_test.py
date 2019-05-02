import unittest
from func import calc_sum, calc_div, calc_mult, calc_diff


class CalcTest(unittest.TestCase):

    def test_calc_sum(self):
        result = calc_sum(1, 2)
        self.assertEqual(result, 3)

    def test_calc_div(self):
        result = calc_div(2, 2)
        self.assertEqual(result, 1)

    def test_calc_mult(self):
        result = calc_mult(5, 5)
        self.assertEqual(result, 25)

    def test_calc_diff(self):
        result = calc_diff(9, 9)
        self.assertEqual(result, 0)

    def test_calc_div_exception(self):
        with self.assertRaises(ZeroDivisionError):
            calc_div(5, 1)