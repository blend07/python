from abc import ABC,abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def sleep(self):
        print(f"{self.name} is sleeping...")

    
class Dog(Animal):
    def make_sound(self):
        print(f"{self.name} says woof woof!")
    def move(self):
        print(f"{self.name} is moving")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} ciu ciu!")
    def move(self):
        print(f"{self.name}")


def describe_animal(Animal):
    Animal.make_sound()
    Animal.move()
    Animal.sleep()

animals = [
    Dog("Buddy"),
    Bird("Sky")
]

for kafshet in animals:
    print("Animal informations:")
    describe_animal(kafshet)