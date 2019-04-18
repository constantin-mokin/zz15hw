# import random
# n = int(input('n:   '))
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(n):
#         row.append(random.randint(1, 9))
#     matrix.append(row)
# print(matrix)
#
# summ = 0
# for row in matrix:
#     for elem in row:
#         if not elem % 3:
#             summ += elem
# print(summ)

#
#
# import random
# n = int(input('n:   '))
# m = int(input('m:   '))
# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(random.randint(0, 9))
#     matrix.append(row)
# print(matrix)
#
# seven = 0
# for row in matrix:
#     for elem in row:
#         if elem == 7:
#             seven += 1
# print(seven)

# #
# import random
# n = int(input('n:   '))
# m = int(input('m:   '))
# matrix_A = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(random.randint(0, 9))
#     matrix_A.append(row)
#     print(matrix_A[i])
#
# summ_elem = 0
# for row in matrix_A:
#     for elem in row:
#         summ_elem += elem
# arif = m * n
# average = summ_elem / arif
# print(average)
#
# count = 0
# for i, row in enumerate(matrix_A):
#     for j, elem in enumerate(row):
#         if elem > average and (i + j) % 2 == 0: #if elem > average and NOT (i + j) % 2
#             count += 1
# print(count)
#
#
# lastname = ['Petrova', 'Ivanova', 'Cvetkova', 'Romanova', 'Turova', 'Andreeva', 'Korneeva', 'Perevalova']
# for lastname in lastname:
#     if lastname[0] == 'P' and lastname[-1] == 'a':
#         print(lastname)


#
#
# pupils = [
#   {
#         'firstname': 'Masha',
#         'group': '41',
#         'physics': 7,
#         'informatics': 6,
#         'history': 8,
#   },
#   {
#         'firstname': 'Evgen',
#         'group': '42',
#         'physics': 1,
#         'informatics': 2,
#         'history': 1,
#   },
#   {
#         'firstname': 'Olga',
#         'group': '43',
#         'physics': 9,
#         'informatics': 9,
#         'history': 9,
#   },
#   {
#         'firstname': 'Serg',
#         'group': '44',
#         'physics': 8,
#         'informatics': 8,
#         'history': 3,
#   },
#   {
#         'firstname': 'Artem',
#         'group': '45',
#         'physics': 8,
#         'informatics': 8,
#         'history': 3,
#   }]
#
# for pupil in pupils:
#     average = (pupil['physics'] + pupil['informatics'] + pupil['history']) / 3
#     if average > 4:
#         for key, value in pupil.items():
#             print(f'{key}: {value}')
#         print('*-*')
#

