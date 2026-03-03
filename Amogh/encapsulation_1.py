"""
 In Python, Encapsulation is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class),
while restricting direct access to some of the object's components.

This is mainly done using getters and setters, focusing on data hiding
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private member

    # getter to get the bank balance
    def get_balance(self):
        print(f"Your current balance is {self.__balance}")
    
    #setter to set the bank balance (deposit) without changing the actual variable
    def set_add_balance(self, amount):
        if(amount>0):
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}")
        else:
            print(f"Cannot deposit the amount {amount}. Please enter a valid amount")


# instance and usage:
myAccount = BankAccount("Amogh",1000)

myAccount.get_balance()
myAccount.set_add_balance(500)