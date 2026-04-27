from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def operation(self): ...

class CComponent(Component):
    def operation(self):
        return "Concrete Component operation"

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        return self.component.operation()

class CDecorator(Decorator):
    def __init__(self, component):
        super().__init__(component)

    def operation(self):
        return f"Decorator operation, {super().operation()}"

# Example Usage:
component = CComponent()
decorator = CDecorator(component)
print(decorator.operation())  # Output: Decorator operation, Concrete Component operation