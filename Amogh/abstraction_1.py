'''
A simple payment processor implementing the concept of abstraction in Python.
The idea is to build a checkout system for an imaginary store that accepts 2 methods:
Credit Card and PayPal.

'''

from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, balance,amount):
        self.balance = balance
        self.amount = amount

    @abstractmethod
    def verify_funds(): #use this inside each payment method to verify the funds
        pass

    @abstractmethod
    def execute_transaction():
        pass

    def make_payment(self): #makes sure the payment workflow is in consistent order
        if self.verify_funds():
            self.execute_transaction()

class CreditCard(Payment):

    def __init__(self, balance, amount):
        super().__init__(balance, amount)

    def verify_funds(self):
        if(self.balance >= self.amount):
            print("Credit card verification successful for amount",self.amount)
            return True
        else:
            print("Credit card declined due to insufficient balance!")

    def execute_transaction(self):
        print("Credit card payment executing...\nCompleted.")

class PayPal(Payment):
    def __init__(self, balance, amount):
        super().__init__(balance,amount)

    def verify_funds(self):
        if(self.balance >= self.amount):
            print("PayPal verification successful for amount",self.amount)
            return True
        else:
            print("Paypal payment failed due to insufficient balance!")

    def execute_transaction(self):
        print("PayPal payment underway...")

pp_user1 = PayPal(200,10000)
pp_user1.make_payment()

cc_user1 = CreditCard(10000,200) 
cc_user1.make_payment() 