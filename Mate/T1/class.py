'''
Task:
Define a class Vehicle with the following attributes and methods:

make (string)

model (string)

display() method to print vehicle details.

Create an instance of Vehicle and call display().
'''

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display(self):
        print(self.make + " " + self.model)

    def __str__(self):
        return self.make + " " + self.model

    def __repr__(self):
        return self.make + " " + self.model

v = Vehicle("Toyota", "Corolla")
assert v.make == "Toyota"
assert v.model == "Corolla"
assert str(v) == 'Toyota Corolla'
assert repr(v) == 'Toyota Corolla'
v.display()


