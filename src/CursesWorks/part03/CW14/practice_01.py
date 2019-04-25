# #task01
#
# from abc import ABC, abstractmethod
#
# class Pet:
#
#
#     def __init__(self, name, age, master, weight, height):
#         self.name = name
#         self.age = age
#         self.master = master
#         self.weight = weight
#         self.height = height
#
#     @abstractmethod
#     def voice(self):
#         pass
#
#
# class Horse(Pet):
#     def voice(self):
#         print('Igogo')
#
# class Donkey(Pet):
#     def voice(self):
#         print('iaiaiai')
#
# class Mule(Donkey, Horse):
#     pass
#
# class Dog(Pet):
#
#     def bark(self):
#         print('Woof!')
#
# class Cat(Pet):
#
#     def meow(self):
#         print('Meow!')
#
# class Parrot(Pet):
#
#     def voice(self):
#         print('Kar')
#
#
# def main():
#
#     dog1 = Dog('Bob', 15, 'Robin', 20, 55)
#     cat1 = Cat('Mars', 3, 'July', 8, 25)
#     parrot1 = Parrot('Koko', 6, 'Mike', 0.025, 15)
#
#     horse1 = Horse('QC', 8, 'REE', 20, 20)
#     donkey1 = Donkey('ZX', 8, 'REE', 20, 20)
#     mule1 = Mule('FF', 1, 'REE', 1, 1)
#     mule1.voice()
#     parrot1.voice()
#
# if __name__ == '__main__':
#     main()
#
#
#######################


#task011


# from abc import ABC, abstractmethod
#
# class A(ABC):
#    @abstractmethod
#    def do_smth(self):
#        print('I am a parent')
# class B(A):
#    def do_smth(self):
#        print('I am a child')
# a = A() # ERROR
# b = B()

