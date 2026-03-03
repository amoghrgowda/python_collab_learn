'''
Exercise 3: Encapsulation
Task:
Create a Passenger class with private attributes name and ticket_id.

Use property decorators to get and set name while keeping ticket_id read-only
'''

class Passenger:
    def __init__(self, name, ticket_id):
        self.__name = name  # TODO: Initialize private attributes
        self.__ticket_id = ticket_id

    @property
    def name(self):
        return self.__name  # TODO: Implement getter; we can control how its accessed
    
    # to make ticket_id read-only, we only provide a getter and no setter
    @property 
    def ticket_id(self): 
        return self.__ticket_id

    @name.setter
    def name(self, new_name):
        self.__name = new_name  # TODO: Implement setter

passenger = Passenger("Bob", "T4567")
assert passenger.name == "Bob"
passenger.name = "Charlie"
assert passenger.name == "Charlie"

# Error because ticket_id is read-only
# passenger.ticket_id = "T67890"  