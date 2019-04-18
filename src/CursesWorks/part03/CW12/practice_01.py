# #task01
#
# class Dog:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#     def bark(self):
#         print('Woof!')
#     def jump(self):
#         print('Jump Bob')
#     def run(self):
#         print('Run Bob, run')
#     def birthday(self):
#         self.age += 1
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#     def meow(self):
#         print('Meow!')
#     def jump(self):
#         print('Jump Mars')
#     def run(self):
#         print('Run Mars, run')
#     def birthday(self):
#         self.age += 1
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#     def fly(self):
#         print('Fly Koko')
#     def jump(self):
#         print('Jump Koko')
#     def run(self):
#         print('Run Koko, run')
#     def birthday(self):
#         self.age += 1
#
# def main():
#
#     dog1 = Dog('Bob', 2, 'Robin')
#     cat1 = Cat('Mars', 3, 'July')
#     parrot1 = Parrot('Koko', 6, 'Mike')
#
# if __name__ == '__main__':
#     main()
#
#####################################
# # task02
#
# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def jump(self):
#         print('Jump!')
#
#     def run(self):
#         print('Run-run-run')
#
#     def birthday(self):
#         self.age += 1
#
# class Dog(Pet):
#
#     def bark(self):
#         print('Woof!')
#
#
# class Cat(Pet):
#
#     def meow(self):
#         print('Meow!')
#
# class Parrot(Pet):
#
#     def fly(self):
#         print('Fly')
#
# def main():
#
#     dog1 = Dog('Bob', 2, 'Robin')
#     cat1 = Cat('Mars', 3, 'July')
#     parrot1 = Parrot('Koko', 6, 'Mike')
#
#     dog1.bark()
#     cat1.meow()
#     parrot1.fly()
#
#     print(dog1.name)
#     print(cat1.name)
#     print(parrot1.name)
#
# if __name__ == '__main__':
#     main()
#
#############################################

# task03
#
# class Pet:
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def jump(self):
#         print('Jump!')
#
#     def run(self):
#         print('Run-run-run')
#
#     def birthday(self):
#         self.age += 1
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.2
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.2
#
# class Dog(Pet):
#
#     def bark(self):
#         print('Woof!')
#
#
# class Cat(Pet):
#
#     def meow(self):
#         print('Meow!')
#
# class Parrot(Pet):
#
#     def fly(self):
#         if self.weight > 0.1:
#             print('This parrot can not fly')
#
# def main():
#
#     dog1 = Dog('Bob', 2, 'Robin', 20, 55)
#     cat1 = Cat('Mars', 3, 'July', 8, 25)
#     parrot1 = Parrot('Koko', 6, 'Mike', 1, 15)
#
#     dog1.bark()
#     cat1.meow()
#     parrot1.fly()
#
#     print(dog1.name)
#     print(cat1.name)
#     print(parrot1.name)
#
#
# if __name__ == '__main__':
#     main()
#
#
#######################################

# # task04
#
# class Pet:
#
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     def jump(self):
#         print('Jump!')
#
#     def run(self):
#         print('Run-run-run')
#
#     def birthday(self):
#         self.age += 1
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.2
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.2
#
# class Dog(Pet):
#
#     def bark(self):
#         print('Woof!')
#
#
# class Cat(Pet):
#
#     def meow(self):
#         print('Meow!')
#
# class Parrot(Pet):
#
#     def fly(self):
#         if self.weight > 0.1:
#             print('This parrot can not fly')
#         else:
#             print('Fly')
#
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.05
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.05
#
# def main():
#
#     dog1 = Dog('Bob', 2, 'Robin', 20, 55)
#     cat1 = Cat('Mars', 3, 'July', 8, 25)
#     parrot1 = Parrot('Koko', 6, 'Mike', 0.025, 15)
#
#     print(parrot1.weight)
#     parrot1.change_weight()
#     print(parrot1.weight)
#
#     parrot1.fly()
#
# if __name__ == '__main__':
#     main()

##################

# task05

# class Pet:
#
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#         self.is_alive = True
#
#     def jump(self):
#         print('Jump!')
#
#     def run(self):
#         print('Run-run-run')
#
#     def birthday(self):
#         self.age += 1
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.2
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.2
#
# class Dog(Pet):
#
#     def bark(self):
#         print('Woof!')
#
#     def birthday(self):
#         if self.is_alive: #### vot ono!!!
#             super().birthday()
#             if self.age > 13:
#                 self.is_alive = False
#
# class Cat(Pet):
#
#     def meow(self):
#         print('Meow!')
#
#     def birthday(self):
#         super().birthday()
#         if self.age > 16:
#             self.is_alive = False
#
# class Parrot(Pet):
#
#     def fly(self):
#         if self.weight > 0.1:
#             print('This parrot can not fly')
#         else:
#             print('Fly')
#
#
#     def change_weight(self, weight=None):
#         if weight:
#             self.weight = weight
#         else:
#             self.weight += 0.05
#
#     def change_height(self, height=None):
#         if height:
#             self.height = height
#         else:
#             self.height += 0.05
#
#     def birthday(self):
#         super().birthday()
#         if self.age > 60:
#             self.is_alive = False
#
# def main():
#
#     dog1 = Dog('Bob', 15, 'Robin', 20, 55)
#     cat1 = Cat('Mars', 3, 'July', 8, 25)
#     parrot1 = Parrot('Koko', 6, 'Mike', 0.025, 15)
#
#     print(dog1.age)
#     dog1.birthday()
#     print(dog1.is_alive)
#
# if __name__ == '__main__':
#     main()

##############




