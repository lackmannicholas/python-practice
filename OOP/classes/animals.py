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


monkey = Monkey("Jojo")
monkey.eat()
monkey.climb()

bird = Bird("Jerry")
bird.eat()
bird.fly()
bird.sleep()