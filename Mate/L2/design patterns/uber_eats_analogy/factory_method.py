'''
Factory Method Pattern Example: Uber Eats Payment Methods
'''

import singleton

# ============================
# Payment Interface
# ============================
class PaymentMethod:
    def process(self, order):
        raise NotImplementedError("Subclasses must implement process()")

# ============================
# Concrete Payment Methods
# ============================
class CreditCardPayment(PaymentMethod):
    def __init__(self):
        config = singleton.UberEatsConfig()
        self.currency = config.currency

    def process(self, order):
        print(f"[CreditCard] Charging {order['total']} {self.currency}...")


class PayPalPayment(PaymentMethod):
    def __init__(self):
        config = singleton.UberEatsConfig()
        self.region = config.region

    def process(self, order):
        print(f"[PayPal] Processing PayPal payment for region {self.region}...")


class ApplePayPayment(PaymentMethod):
    def __init__(self):
        config = singleton.UberEatsConfig()
        self.api_key = config.api_key

    def process(self, order):
        print(f"[ApplePay] Using API key {self.api_key} to process Apple Pay...")


# ============================
# Factory Method
# ============================
class PaymentFactory:
    @staticmethod
    def create(method: str) -> PaymentMethod:
        method = method.lower()

        if method == "card":
            return CreditCardPayment()

        if method == "paypal":
            return PayPalPayment()

        if method == "apple":
            return ApplePayPayment()

        raise ValueError(f"Unknown payment method: {method}")

