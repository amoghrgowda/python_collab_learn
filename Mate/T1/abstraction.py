'''
if you want to override any method in the parent class, you must implement it in the child class.
'''

from abc import ABC, abstractmethod

class TransportUser(ABC):
    @abstractmethod
    def travel(self):
        pass  # TODO: Enforce implementation in subclasses

class Commuter(TransportUser):
    def travel(self): # have their own implementation of the travel method, which is required by the abstract base class
        return "Traveling by bus"


commuter = Commuter()
 
assert commuter.travel() == "Traveling by bus"

print(commuter.travel()) 

