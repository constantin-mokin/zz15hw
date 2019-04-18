# #task_01
# class Dog:
#     pass
#
# dog = Dog()
#
########################
# #task02
#
# class Dog:
#     pass
#
# dog1 = Dog()
# print(dog1)
#
# dog2 = Dog()
# print(dog2)

###########################
# #task03
#
# class Dog:
#     def bark(self):
#         print('Woof, Woof!')
#     def jump(self):
#         print('Jump Dog')
#     def run(self):
#         print('Run Vasya, RUN!!!')
#
# dog1 = Dog()
# dog1.bark
# print(dog1)
#
# dog2 = Dog()
# dog2.jump()
# print(dog2)
#
# dog3 = Dog()
# dog3.run()
# print(dog3)

##########################
#
#
# #task04
#
# class Dog:
#     def __init__(self, name, height, weight, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
# dog1 = Dog('Bob', 60, 35, 8)
# # print(dog1.name)
# # print(dog1.height)
# # print(dog1.weight)
# # print(dog1.age)
# print(dog1.name, dog1.height, dog1.weight, dog1.age)
#
# dog2 = Dog('Jack', 45, 22, 4)
# print(dog2.name, dog2.height, dog2.weight, dog2.age)

# #task05
#
# class Dog:
#     def __init__(self, name, height, weight, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#     def change_name(self, name):
#         self.name = name
#
# dog1 = Dog('Bob', 60, 35, 8)
# print(dog1.name, dog1.height, dog1.weight, dog1.age)
#
# dog1.change_name('Jack')
# print(dog1.name, dog1.height, dog1.weight, dog1.age)
#
#
#########################################
# #task06
#
# class Dog:
#     def __init__(self, name, height, weight, age, master):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self.__master = master
#
#     def change_name(self, name):
#         self.name = name
#
#     def get_master(self):
#         return self.__master
#
# dog1 = Dog('Bob', 60, 35, 8, 'Robin')
# print(dog1.name, dog1.height, dog1.weight, dog1.age)
#
# dog1.change_name('Jack')
# print(dog1.name, dog1.height, dog1.weight, dog1.age)
#
# print(dog1.get_master())

############################

# #task07
#
# class Dog:
#     def __init__(self, name, height, weight, age, master, location='Minsk'):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#         self.__master = master
#         self.__location = location
#
#     def change_name(self, name):
#         self.name = name
#
#     def get_master(self):
#         return self.__master
#
#     def get_location(self):
#         return self.__location
#     def set_location(self, location):
#         self.__location = location
#
# adress = Dog('Bob', 50, 20, 5, 'Robin', 'Minsk')
# print(adress.get_location())
# adress.set_location('Logoisk')
# print(adress.get_location())

# #task08
#
# class Dog:
#     def __init__(self, name, height, weight, age, master, location='Minsk'):
#         self.__name = name
#         self.__height = height
#         self.__weight = weight
#         self.__age = age
#         self.__master = master
#         self.__location = location
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def height(self):
#         return self.__height
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @property
#     def age(self):
#         return self.__age
#
#     @property
#     def master(self):
#         return self.__master
#
#     @property
#     def location(self):
#         return self.__location
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @master.setter
#     def master(self, master):
#         self.__master = master
#
#     @location.setter
#     def location(self, location):
#         self.__location = location
#
# dog = Dog('Bob')
#





