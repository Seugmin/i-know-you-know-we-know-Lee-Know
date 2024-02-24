class Animal:
    def __init__(self, name , species, legs):
        self.name = input("name:")
        self.species = "Animal"
        self.legs = 4

    def voice(self):
        print("voice")

    def runing(self):
        print("Animal il runing")


class Dog(Animal):
    breed = "shepherd"

    def bark(self, bark):
        self.bark = "bark"


class Bird(Animal):
    wingspan = 50

    def __init__(self, name, wingspan):
        self.name = "Barsik"
        self.wingspan = 50

dog = Dog("shepherd")
bird = Bird("Barsik")
d = Dog
b = Bird
d.bark()
b.wingspan()