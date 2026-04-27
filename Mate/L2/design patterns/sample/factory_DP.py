from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self): ...

class CProduct(Product):
    def operation(self):
        return "Concrete Product Operation"

class Factory:
    @abstractmethod
    def create_product(self):
        pass

class CFactory(Factory):
    def create_product(self):
        return CProduct()

# Example Usage:
factory = CFactory()
product = factory.create_product()
print(product.operation())  # Output: Concrete Product Operation