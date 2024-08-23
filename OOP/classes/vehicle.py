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

    @staticmethod
    def get_vehicle_count():
        return Vehicle.vehicle_count
    
    def drive(self):
        print("Vehicle driving...")

class Truck(Vehicle):
    def drive(self):
        print("Truck driving...")