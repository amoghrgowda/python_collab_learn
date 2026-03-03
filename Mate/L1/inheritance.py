# Python OOP
'''
This program will focus on inheritance. Inheritance is a fundamental concept in object-oriented programming that allows a new class (called a child class or subclass) to inherit attributes and methods from an existing class (called a parent class or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
'''

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first +"_"+last + "@company.com"

    def print_fullname(self):
        return self.first+" "+self.last
        
    def __str__(self):
        return f'\nEmployee Details: \nFull name:{self.first} {self.last}, Salary: {self.salary}, Email: {self.email}'

class Developer(Employee):
    def __init__(self, first, last, salary, programming_language):
        super().__init__(first, last, salary) # this will call the init method of the parent class
        self.programming_language = programming_language

    def __str__(self):
        return f'\nDeveloper Details: \nFull name:{self.first} {self.last}, Salary: {self.salary}, Email: {self.email}, Programming Language: {self.programming_language}'
    
emp1 = Developer('Amogh', 'R.Gowda', 50000, 'Java')
emp2 = Developer('Test', '1', 80000, 'Python')

print(emp1)
print(emp2)
