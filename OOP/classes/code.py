class Vehicle:
    # class attributes
    vehicle_count = 0

    def __init__(self, body_type, make) -> None:
        # instance attributes
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_count += 1
        self.vehicle_number = Vehicle.vehicle_count
        pass

    def get_vehicle_count(self):
        return Vehicle.vehicle_count

car = Vehicle(body_type="four door sedan", make="fiat")
truck = Vehicle(body_type="truck", make="ford")

print(car.vehicle_body)
print(car.vehicle_number)
print(truck.vehicle_body)
print(truck.vehicle_number)
print(Vehicle.get_vehicle_count())