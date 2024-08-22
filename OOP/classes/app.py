from vehicle import Vehicle, Truck

car = Vehicle(body_type="four door sedan", make="fiat")
truck = Truck(body_type="truck", make="ford")

print(car.vehicle_body)
print(car.vehicle_number)
print(truck.vehicle_body)
print(truck.vehicle_number)
print(Vehicle.get_vehicle_count())