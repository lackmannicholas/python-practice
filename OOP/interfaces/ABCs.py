
'''
    You can use the python abstract base class library to create formal interfaces.
    Here you can see that while the subclass check returns true, instantiating a class of Bird raises the NotImmplementedError
    giving programmers immediate feedback as to what part of the interface contract is not implemented.
'''
import abc

class IAnimal(metaclass=abc.ABCMeta):
    def __init__(self, name) -> None:
        self.animal_name = name

    @classmethod
    def __subclasshook__(self, subclass: type) -> bool:
        return (hasattr(subclass, 'eat') and
                callable(subclass.eat) and
                hasattr(subclass, 'sleep') and
                callable(subclass.sleep) or 
                NotImplemented)
    
    @abc.abstractmethod
    def eat(self) -> None:
        raise NotImplementedError("Concrete class has not implemented this method")
    
    @abc.abstractmethod
    def sleep(self) -> None:
        raise NotImplementedError("Concrete class has not implemented this method")
    
class Monkey(IAnimal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.animal_name} is eating bananas")

    def climb(self):
        print(f"{self.animal_name} is climbing")

    def sleep(self):
        print(f"{self.animal_name} is sleeping")

class Bird(IAnimal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.animal_name} is eating seeds")

    def fly(self):
        print(f"{self.animal_name} is flying")


if __name__ == "__main__":
    print(f"Monkey is subclass of Animal: {issubclass(Monkey, IAnimal)}")
    print(f"Bird is subclass of Animal: {issubclass(Bird, IAnimal)}")

    monkey = Monkey("Fred")
    bird = Bird("Joey")
    
