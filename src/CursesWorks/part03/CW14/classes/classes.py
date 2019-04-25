from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def voice(self):
        pass


class Pet(Animal):          #Animal
    pass


class WildAnimal(Animal):   #Animal
    pass


class FelineInterface(ABC):
    @abstractmethod
    def scratch(self):
        raise NotImplemented


class CanineInterface(ABC):
    @abstractmethod
    def swimm(self):
        raise NotImplemented


class Cat(Pet, FelineInterface):
    def voice(self):
        pass


class Dog(Pet, CanineInterface):
    def voice(self):
        pass


class Lion(WildAnimal, FelineInterface):
    def voice(self):
        pass


class Wolf(WildAnimal, CanineInterface):
    def voice(self):
        pass



