'''
Task:
Create a base class Person with an attribute name and a method display().

Create a subclass Driver that inherits from Person and adds a license_number attribute.

Override the display() method in Driver to include license_number.
'''


class Person:
    def __init__(self, name):
        self.name = name  # TODO: Initialize name

    def display(self):
        print(self.name)  # TODO: Print person name

class Driver(Person):
    def __init__(self, name, license_number):
        super().__init__(name) # call the parent constructor to initialize name
        self.license_number = license_number  # TODO: Initialize license_number

    def display(self):
        print(self.name + " " + self.license_number)  # TODO: Print driver details 

driver = Driver("Alice", "D12345")
assert driver.name == "Alice"
assert driver.license_number == "D12345"
