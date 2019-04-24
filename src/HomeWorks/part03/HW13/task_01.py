#task01
##В упор не пойму как делать..
#Это с любыми заданиями
#Если есть перед глазами аналог или пример, то соображаю
#Если нет, то пустота и в мыслях и в глазах..

import random

class Pet:

    __counter = 0  #private

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True
        Pet.__counter += 1      #private

    @staticmethod
    def get_random_name(rnd):

        return

    @classmethod                #decorator
    def get_counter(cls):
        return cls.__counter

    def voice(self):
        pass


class Horse(Pet):
    def voice(self):
        print('Igogo')

class Donkey(Pet):
    def voice(self):
        print('iaiaiai')

class Mule(Donkey, Horse):
    pass



class Dog(Pet):

    def bark(self):
        print('Woof!')

class Cat(Pet):

    def meow(self):
        print('Meow!')

class Parrot(Pet):

    def fly(self):
        if self.weight > 0.1:
            print('This parrot can not fly')
        else:
            print('Fly')


    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.05

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.05

    def birthday(self):
        super().birthday()
        if self.age > 60:
            self.is_alive = False

    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

# main!!!
def main():

    dog1 = Dog('Bob', 15, 'Robin', 20, 55)
    cat1 = Cat('Mars', 3, 'July', 8, 25)
    parrot1 = Parrot('Koko', 6, 'Mike', 0.025, 15, 'RED')

    horse1 = Horse('QC', 8, 'REE', 20, 20)
    donkey1 = Donkey('ZX', 8, 'REE', 20, 20)
    mule1 = Mule('FF', 1, 'REE', 1, 1)

    mule1.voice()

if __name__ == '__main__':
    main()


