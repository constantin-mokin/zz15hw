#task08

class Dog:
    def __init__(self, name, height, weight, age, master, location='Minsk'):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__age = age
        self.__master = master
        self.__location = location

    @property
    def name(self):
        return self.__name

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def age(self):
        return self.__age

    @property
    def master(self):
        return self.__master

    @property
    def location(self):
        return self.__location

    @name.setter
    def name(self, name):
        self.__name = name

    @height.setter
    def height(self, height):
        self.__height = height

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    @age.setter
    def age(self, age):
        self.__age = age

    @master.setter
    def master(self, master):
        self.__master = master

    @location.setter
    def location(self, location):
        self.__location = location

dog = Dog('Bob')

