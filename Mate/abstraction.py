# Python OOP
'''
This program demonstrates abstraction in Python OOP.
Abstraction allows us to hide complex implementation details and show only the necessary features of an object.
In this example, we have an abstract class Employee that defines a method max_loan_amount() which must be implemented by any subclass. 
The borrow_loan() method uses this abstract method to determine if the loan amount requested by the employee is within the allowed limit.
'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "_" + last + "@company.com"

    @abstractmethod
    def max_loan_amount(self):
        """Each employee type must define its own loan limit. It hides how loan limits are calculated."""
        pass

    def borrow_loan(self, amount):
        """General loan borrowing logic shared by all employees."""
        if amount > self.max_loan_amount():
            return (f"Loan denied for {self.first}. "
                    f"Max allowed is {self.max_loan_amount()}")
        return f"{self.first} {self.last} borrowed {amount}"

class Manager(Employee):
    def __init__(self, first, last, salary, department):
        super().__init__(first, last, salary)
        self.department = department

    def max_loan_amount(self):
        return self.salary * 1.5   # Managers can borrow 150%

class Developer(Employee):
    def __init__(self, first, last, salary, programming_language):
        super().__init__(first, last, salary)
        self.programming_language = programming_language

    def max_loan_amount(self):
        return self.salary * 0.8   # Developers can borrow 80%

mgr = Manager("Alice", "Smith", 120000, "Finance")
dev = Developer("Bob", "Jones", 90000, "Python")

print(mgr.borrow_loan(150000))   # allowed (<= 180,000)
print(dev.borrow_loan(80000))    # denied (max 72,000)
