class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.make} {self.model}"

class Driver(Vehicle):
    def __init__(self, make, model, license_number):
        super().__init__(make, model)
        self.license_number = license_number

    def display(self):
        return f"Driver: {self.make} {self.model}, License: {self.license_number}"
        
import unittest

class TestVehicle(unittest.TestCase):
    def test_vehicle_attributes(self):
        v = Vehicle("Toyota", "Corolla")
        self.assertEqual(v.make, "Toyota")
        self.assertEqual(v.model, "Corolla")
        # pass  # TODO: Write test for vehicle attributes

class TestDriver(unittest.TestCase):
    def test_driver_display(self):
        d = Driver("Honda", "Civic", "012345")
        # pass  # TODO: Write test for driver display
        self.assertEqual(d.make, "Honda")
        self.assertEqual(d.model, "Civic")
        self.assertEqual(d.license_number, "012345")

if __name__ == "__main__":
    unittest.main()
