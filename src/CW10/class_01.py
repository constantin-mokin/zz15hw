# #task01
#
# list_a = [1, 2, 3, 4, 5, 6, 7, 8]
#
# result = map (str, list_a)
#
# print(list(result))


# #task02
#
#
# list_names = ['Kate', 'Olga', 'Evgen', 'Konstantin']
#
# result = filter(lambda elem: 'k' in elem or 'K' in elem, list_names)
#
# print(list(result))
#


#task03


# from functools import reduce
#
#### #list_number = [i for i  in [1, 2, 3, 4, 5, 6, 7, 8] if i % 3 == 0] - vse chisla kratnie 3 i vpihivaem v reshenie
#
# result = reduce(lambda a, x: a * x, [i for i  in [1, 2, 3, 4, 5, 6, 7, 8] if i % 3 == 0], 1)
#
# print(result)


###################################
# #task04
#
# my_file = open ('test.txt')
# print(my_file)
# my_file.close()
#
# #task05
#
# my_file = open ('test.txt')
# print(my_file.readline().strip())
# print(my_file.readline())
# my_file.close()
#
# #task06
#
# my_file = open ('test.txt')
# while True:
#     line = my_file.readline() #.strip
#     if not line:
#         break
#     print(line)
# my_file.close()
#
# #task06
#
# my_file = open ('test.txt')
#
# count = 0
# s1 = 1
# s2 = 2
#
# while True:
#     line = my_file.readline().strip()
#     if not line:
#         break
#     count += 1
#
#     if count == 1:
#         print(line)
#
#     if count == 5:
#         print(line)
#
#     if count < 6:
#         print(line)
#
#     if s1 <= count <= s2:
#         print(line)
#
# my_file.close()
#
# #task07
#
# my_file = open ('test.txt')
# print(my_file.readlines())
#
# my_file.close()
#
#
# #task08
#
# with open('test.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)


# #task09
#
# with open('test.txt', 'w') as my_file:
#     my_file.write('qwerty')
#

# #task10
#
# import json
#
# with open('test.txt', 'w') as my_file:
#     data = json.dumps({'a': 5})
#     print(type(data))
#     print(data)
#     my_file.write(data)
#
# with open('test.json', 'w') as my_file:
#     data = json.loads(my_file.read())
#     print(type(data))
#     print(data)












