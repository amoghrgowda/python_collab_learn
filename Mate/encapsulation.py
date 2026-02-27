# Python - OOP 
# Encapslation
'''
Goal is to hide the data and only allow access to it through methods. This is done to protect the data from being modified by outside code and to ensure that the data is only modified in a controlled way. In Python, we can achieve encapsulation by using private and protected variables. Private variables are defined with a double underscore prefix (e.g. __variable) and can only be accessed within the class. Protected variables are defined with a single underscore prefix (e.g. _variable) and can be accessed within the class and its subclasses, but not from outside the class. 
'''
class Employee:
    def __init__(self, employee_id, first, last, role, salary):
        self._employee_id = employee_id # protected 
        self.__first = first # private 
        self.__last = last # private 
        self._role = role # protected 
        self.__salary = salary # private
        self.__email = first +"_"+last + "@company.com" # private

    def print_fullname(self):
        return self.__first+" "+self.__last
        
    def __str__(self):
        return f'\nEmployee Details: \nFull name:{self.__first} {self.__last}, Salary: {self.__salary}, Email: {self.__email}'

emp1 = Employee(1, 'Amogh', 'R.Gowda', 'Manager', 50000)
emp2 = Employee(2, 'Test', '1', 'Developer', 80000)

# print(emp1.__first) # this will give an error because of encapsulation
print(emp1._Employee__first)
print(emp1._Employee__last)
print(emp1._Employee__salary)
print(emp1._Employee__email)