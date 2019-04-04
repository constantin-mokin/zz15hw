# def my_func(name):
#     print(f'Hello, {name}')
#
# list_name = ['Andry', 'Kirill', 'Olga', 'Sveta', 'Anna']
#
# for i in list_name:
#     my_func(i)
#

# #task02-01
#
# def fff(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
#
# print(fff(5))
# print(fff(7))
# print(fff(8))
#
# #task02-02
#
# def fff(n):
#     i = n
#     result = 1
#     while i:
#         result *= i
#         i -= 1
#     return result
# print(fff(5))
# print(fff(7))
# print(fff(8))



# #task 03
#
# from random import randint
#
#
# def create_matrix(n):
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(randint(-10, 10))
#         matrix.append(row)
#     return matrix
#
# print (create_matrix(5))
#
#
#
# def simple_print(matrix):
#     for row in matrix:
#         print(row) #выводим матрицу построчно
#
# matrix_a = create_matrix(5)
# simple_print(matrix_a)
#
#
#
#
# def summ_print(matrix):
#     summ = 0
#     for row in matrix:
#         for i in row:
#             summ += i
#     return summ
#
#
# def max_print(matrix): #НЕ то
#     max_a = []
#     for row in matrix:
#         a = max(row)
#         max_a.append(a)
#     return max_a
#
#
# def min_print(matrix): #НЕ то
#     min_a = []
#     for row in matrix:
#         a = min(row)
#         min_a.append(a)
#     return min_a
#
#

