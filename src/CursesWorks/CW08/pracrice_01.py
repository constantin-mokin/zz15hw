# from typing import Union
#
# def inches_to_cm(n: 'expected types int, float') -> float:
#     """
#     Returns argument n as a representation in cm
#
#     Parameters
#     ----------
#     inches: Union[int, float"
#     some ""
#     return round(n * 2.54, 2)

# task 01
# from random import randint
#
# def create_matrix(n, random_from=1, random_to=9):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(randint(random_from, random_to))
#         matrix.append(row)
#     return matrix
#


#task 02

#
# def print_sum(*args):
#     sum = 0
#     for i in range(len(args)):
#         sum += args[i] * i
#     return sum
#
# print(print_sum(1,2,3,4,5,6,7,8,9))
#
# task 03
#
# def func(*args):
#     return args
#
#
#
# arguments = [1,2,3,4,5,6]
#
# func(*arguments) #распаковываем список
#
# print(func(arguments)) # запаковано
# print()
# print(func(*arguments)) # распаковано

# task 04
# def my_func(*args):
#     sum_args = sum(args)
#     max_args = max(args)
#     return sum_args, max_args
#
#
# arguments = [1,2,3,4,5,6]
#
#
# print(my_func(*arguments))
# print()
# a, b = my_func(1,2,5,4,6,7)

# task 05

# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         if len(key) % 2 == 0:
#         #if not len(key) % 2:
#             print(key, value)
#
#
# arguments = {'ad' : 1, 'b' : 2, 'c' :3, 'rd' : 4,'errrr' :5,'fffff' : 6}
#
# my_func(**arguments)





