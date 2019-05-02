import unittest
from utils import Math


class CalcTest(unittest.TestCase):

    def setUp(self):                #вместо частого заполнения значений
        self.math = Math(16, 4)     #используем это. либо без всего этого, но в кажом будем дописыаать значения

    def test_calc_sum(self):
        #math = Math(5, 4)
        result = math.calc_sum()
        self.assertEqual(result, 9)

    def test_calc_div(self):
        #math = Math(16, 4)
        result = math.calc_div()
        self.assertEqual(result, 4)


#
# import unittest
# from src.cw.cw15.src.func.utils import Math
#
#
# class CalcTest(unittest.TestCase):
#
#     def setUp(self):
#         self.math = Math(16, 4)
#         self.math_div_exc = Math(16, 0)
#
#     def test_calc_sum(self):
#         result = self.math.calc_sum()
#         self.assertEqual(result, 20)
#
#     def test_calc_div(self):
#         result = self.math.calc_div()
#         self.assertEqual(result, 4)
#
#     def test_calc_div_exc(self):
#         with self.assertRaises(ZeroDivisionError):
#             self.math_div_exc.calc_div()

