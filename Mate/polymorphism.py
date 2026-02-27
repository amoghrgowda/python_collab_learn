# Python OOP 

'''
This program will focus on polymorphism. Polymorphism is a fundamental concept in OOP that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying data types. In Python, polymorphism is achieved through method overriding and duck typing. Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass. Duck typing is a concept where the type or class of an object is less important than the methods it defines. If an object implements the required methods, it can be used in place of any other object that implements those methods, regardless of their actual class.
'''


class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + "_" + last + "@company.com"

    def max_loan_amount(self):
        return self.salary * 0.5   # base employees can borrow 50% of salary

    def borrow_loan(self, amount):
        if amount > self.max_loan_amount():
            return f"Loan denied for {self.first}. Max allowed is {self.max_loan_amount()}"
        return f"{self.first} {self.last} has borrowed a loan of {amount}"

    
class Manager(Employee):
    def __init__(self, first, last, salary, department):
        super().__init__(first, last, salary)
        self.department = department

    def max_loan_amount(self):
        return self.salary * 1.5   # managers can borrow 150% of salary

    def borrow_loan(self, amount):
        if amount > self.max_loan_amount():
            return f"Loan denied for Manager {self.first}. Max allowed is {self.max_loan_amount()}"
        return f"{self.first} {self.last} borrowed {amount} for the {self.department} department"


class Developer(Employee):
    def __init__(self, first, last, salary, programming_language):
        super().__init__(first, last, salary)
        self.programming_language = programming_language

    def max_loan_amount(self):
        return self.salary * 0.8   # developers can borrow 80% of salary

    def borrow_loan(self, amount):
        if amount > self.max_loan_amount():
            return f"Loan denied for Developer {self.first}. Max allowed is {self.max_loan_amount()}"
        return f"{self.first} {self.last} borrowed {amount} for a new laptop"


emp = Employee("Amogh", "R.Gowda", 50000) 
mgr = Manager("Alice", "Smith", 120000, "Finance") 
dev = Developer("Bob", "Jones", 90000, "Python") 

print(emp.borrow_loan(20000)) # allowed (<= 25,000) 
print(mgr.borrow_loan(200000)) # allowed (<= 180,000) 
print(dev.borrow_loan(80000)) # denied (max 72,000)