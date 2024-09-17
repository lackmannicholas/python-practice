
'''
    You can use a Meta type to come closer to a strict interface in python.
    A Meta class is a class that is used to define the type of another class and inherits from type. 
    We will overwrite the isinstance and issubclass methods and use this meta type as the metaclass in our concrete classes.
'''
from typing import Any, List


class AnimalMeta(type):
    def __instancecheck__(self, instance: Any) -> bool:
        # pass this instance check to the subclass check to enforce the more strict checking
        return self.__subclasscheck__(instance)
    
    def __subclasscheck__(self, subclass: type) -> bool:
        return (hasattr(subclass, 'eat') and
                callable(subclass.eat) and
                hasattr(subclass, 'sleep') and
                callable(subclass.sleep))
    
class Animal(metaclass=AnimalMeta):
    def __init__(self, name) -> None:
        self.animal_name = name
    
class Monkey(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.animal_name} is eating bananas")

    def climb(self):
        print(f"{self.animal_name} is climbing")

    def sleep(self):
        print(f"{self.animal_name} is sleeping")

class Bird(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.animal_name} is eating seeds")

    def fly(self):
        print(f"{self.animal_name} is flying")


if __name__ == "__main__":
    print(f"Monkey is subclass of Animal: {issubclass(Monkey, Animal)}")
    print(f"Bird is subclass of Animal: {issubclass(Bird, Animal)}")

    