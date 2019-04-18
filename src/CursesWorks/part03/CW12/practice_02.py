# task05

class Pet:

    def __init__(self, name, age, master, weight, height):
        self.name = name
        self.age = age
        self.master = master
        self.weight = weight
        self.height = height
        self.is_alive = True

    def jump(self):
        print('Jump!')

    def run(self):
        print('Run-run-run')

    def birthday(self):
        self.age += 1

    def change_weight(self, weight=None):
        if weight:
            self.weight = weight
        else:
            self.weight += 0.2

    def change_height(self, height=None):
        if height:
            self.height = height
        else:
            self.height += 0.2

class Dog(Pet):

    def bark(self):
        print('Woof!')

    def birthday(self):
        if self.is_alive: #### vot ono!!!
            super().birthday()
            if self.age > 13:
                self.is_alive = False

class Cat(Pet):

    def meow(self):
        print('Meow!')

    def birthday(self):
        super().birthday()
        if self.age > 16:
            self.is_alive = False

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

    print(parrot1.species)

if __name__ == '__main__':
    main()


