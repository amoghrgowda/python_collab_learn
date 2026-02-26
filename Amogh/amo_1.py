# Python OOP - This program will focus on classes and instances
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

emp1 = Employee('Amogh', 'R.Gowda', 50000)
emp2 = Employee('Test', '1', 80000)

# print('{} {}'.format(emp1.first,emp1.last))

# print('Employee 1: {} and Employee 2: {}'.format(emp1.print_fullname(),emp2.print_fullname()))

print(emp1)
print(emp2)