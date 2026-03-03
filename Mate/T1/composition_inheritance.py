class TransportCompany:
    def __init__(self):
        self.vehicles = []  # TODO: Initialize a list of vehicles

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)  # TODO: Add vehicle to transport company

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

company = TransportCompany()
vehicle = Vehicle("Tesla", "Model S")
company.add_vehicle(vehicle)
assert vehicle in company.vehicles
