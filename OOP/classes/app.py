from vehicle import Vehicle, Truck
from animals import Monkey, Bird

car = Vehicle(body_type="four door sedan", make="fiat")
truck = Truck(body_type="truck", make="ford")

print(car.vehicle_body)
print(car.vehicle_number)
print(truck.vehicle_body)
print(truck.vehicle_number)
print(Vehicle.get_vehicle_count())

for v in [car, truck]:
    v.drive()

monkey = Monkey("Jojo")
monkey.eat()
monkey.climb()

bird = Bird("Jerry")
bird.eat()
bird.fly()
bird.sleep()