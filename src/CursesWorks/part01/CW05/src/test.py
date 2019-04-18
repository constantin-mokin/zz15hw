# # Получить сумму кубов натуральных чисел
# n = int(input('--->  '))
# i = 1 # только натуральные числа, 0 не натуральное число, а целое
# summ = 0
# while i <= n:
#         summ += i ** 3
#         i += 1
# print(summ)



#Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7
# import random
#
#
# while True:
#     n = random.randint(0, 10)
#     if n == 7:
#         break
#     print(n)
#
# from random import randint
# while True:
#     n = randint(0, 10)
#     if n == 7:
#         break
#     print(n)



# n = int(input('---> start '))
# m = int(input('---> stop '))
# summ = 0
# for i in range(n, m):
#     i**3
# print(summ)


# from random import randint
# matrix = []
# n = int(input('--->  '))
#
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(str(randint(1, 9))) #Приведение типов!! числа переводим в строки!!!
#     matrix.append(row)
# #print(matrix) #в одну строку
#
# for i in range (n): #красивая матрица со скобками
#     #print(matrix[i])
#     print(' '.join(matrix[i])) # ПЕЧАТАЕМ #Приведение типов!! числа переводим в строки!!!
#                                 # получаем красивую матрицу без скобок



# from random import randint
# matrix = []
# n = int(input('--->  '))
# summ = 0
#
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(randint(1, 9))
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] % 3 == 0:
#             summ += matrix[i][j]
# print(summ)
#
#
#
#
