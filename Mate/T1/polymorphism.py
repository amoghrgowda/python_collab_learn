'''
Task:
Modify Person and create a subclass Cyclist.

Override ride() so that Person can ride for a standard distance, and Cyclist can ride for an extended distance.
'''

class Person:
    def __init__(self, distance=10): 
        self.distance = distance
        
    def ride(self):
        return f"Riding for {self.distance} km"

class Cyclist(Person):
    def __init__(self):
        super().__init__(distance=50)  # Initialize with extended distance

person = Person()
cyclist = Cyclist()
assert person.ride() == "Riding for 10 km"
assert cyclist.ride() == "Riding for 50 km"
