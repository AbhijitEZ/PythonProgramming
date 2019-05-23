from abc import ABC, abstractmethod


class Car:
    default_value = "All remain same"  # static

    def __init__(self, wheels_count=2):
        self.wheels_count = wheels_count  # property

    def __str__(self):
        # default function is when calling print
        return(f"This is default print")

    def __eq__(self, other):
        # equality check magic method for the object
        return self.wheels_count == other.wheels_count

    @classmethod
    def zeroWheel(cls):  # class method, cls points to the class itself
        return cls(0)

    def wheels(self, wheels_count):  # method
        self.wheels_count = wheels_count
        print(f"{wheels_count} number of wheels")


Car.default_value = "changed"
honda = Car(4)

print(honda.default_value)
honda.default_value = "lamda"
honda.wheels(15)
another = Car(3)
print(another.default_value)

nullWheel = Car.zeroWheel()
print(nullWheel)

# equality check magic method for the object
jeep = Car(4)
maruti = Car(4)
print(jeep == maruti)


# Container like representation in class
class TagCloud:

    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("PythOn")
print(cloud.tags)


class Product:
    def __init__(self, price):
        self.__price = price

    def getItem(self):
        return self.__price   # private property

    def setIntem(self, value):
        self.__price = value


dust = Product(10)
print(dust.getItem())


# inheritance
class Animal:
    def eat(self):
        print("eat")


class Human(Animal):
    def walk(self):
        print("walk")


John = Human()
John.walk()
John.eat()


# abstract
class Mammal(ABC):
    def eat(self):
        print("FOOD")

    @abstractmethod
    def walk(self):
        pass  # used when there is no implemetation


class Bear(Mammal):
    def walk(self):
        print("With 4 legs")


lupa = Bear()
lupa.walk()
