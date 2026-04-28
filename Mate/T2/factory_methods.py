
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} payment through Credit Card."

class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} payment through PayPal."

class BankTransferPayment(Payment):
    def process_payment(self, amount):
        return f"Processing ${amount} payment through Bank Transfer."

class PaymentFactory:
    _payment_methods = {
        "credit": CreditCardPayment,
        "paypal": PayPalPayment,
        "bank": BankTransferPayment,
    }

    @staticmethod
    def get_payment_method(method):
        if method in PaymentFactory._payment_methods:
            return PaymentFactory._payment_methods[method]() # used to initialize the class object
        else:
            raise ValueError("Unsupported payment method")


def process_from_user_input():
    method = input("Enter payment method (credit/paypal/bank): ").strip().lower()

    try:
        payment_processor = PaymentFactory.get_payment_method(method)
        print(payment_processor.process_payment(100))
    except ValueError as e:
        print(e)

def fetch_config():
    return ("credit", 10) # here's dummy code. in real-life, we may be reading from a configuration file

def process_from_external_input():
  method, amount = fetch_config() 
  try:
      payment_processor = PaymentFactory.get_payment_method(method)
      print(payment_processor.process_payment(amount))
  except ValueError as e:
      print(e)

process_from_user_input()
process_from_external_input()