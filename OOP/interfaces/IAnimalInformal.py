
'''
    You can use an informal abstract class to implement an informal interface.
    An informal abstract class is a class that defines methods but does not provide an implementation. In Python abstract classes are by default informal
    because there is no 'abstract' class modifier. 
    Here we are using an informal abstract animal class to define eat and sleep methods.
    This does not strictly enforce a typical interface implementation because, as you can see, neither Monkey or Bird implement the sleep method
    therefore breaking the interface contract.
'''
class Animal:
    def __init__(self, name) -> None:
        self.animal_name = name

    def eat(self) -> None:
        raise NotImplementedError("Concrete class has not implemented this method")
    
    def sleep(self) -> None:
        raise NotImplementedError("Concrete class has not implemented this method")
    
class Monkey(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def eat(self):
        print(f"{self.animal_name} is eating bananas")

    def climb(self):
        print(f"{self.animal_name} is climbing")

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
    