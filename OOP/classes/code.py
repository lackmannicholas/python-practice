class Vehicle:
    def __init__(self, body_type, make) -> None:
        self.vehicle_body = body_type
        self.vehicle_make = make
        pass

car = Vehicle(body_type="four door sedan", make="fiat")
truck = Vehicle(body_type="truck", make="ford")

print(car.vehicle_body)
print(truck.vehicle_body)
