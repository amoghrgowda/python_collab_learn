'''
Decorators
- Decorators wraps objects to attach new behaviors.

A decorator must:
    1. Hold a reference to another object
    2. Delegate calls to that object
    3. Add behavior around that delegation

Pros:
    Allows behaviour to be added to objects dynamically.
    Promotes code reuse by allowing decorators to be applied to different components.
    Supports the Single Responsibility Principle by separating concerns into individual decorators.

Cons:
    Can lead to a large number of small classes if not managed carefully.
    Can make it difficult to understand the behaviour of objects due to the dynamic addition of responsibilities.
'''
import time
from datetime import datetime

 # Concrete component - represents objects to which additional responsibilities can be added
class Printer:
  def print(self, text):
    print(f"[LOG] {text}")

# ConcreteDecorator - adds additional responsibilities to the component by calling its operation method and adding extra behaviour.
# -- Wraps another printer
class TimestampDecorator:
  def __init__(self, printer):
    self.printer = printer

  def print(self, text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    self.printer.print(f"{timestamp} - {text}") # Delegates the call to the wrapped printer and adds a timestamp before the message

def printTestMessages(printer):  
  printer.print("First Test message")
  printer.print("Second Test message")
  printer.print("Third Test message")


def printTimeSensitiveTestMessages(printer):
  printer.print(" First Test message")
  time.sleep(1)
  printer.print(" Second Test message")
  time.sleep(1)
  printer.print(" Third Test message")
  time.sleep(1)
  printer.print(" Fourth test message")

logger = Printer()
printTestMessages(logger)

# we can add the additional behavior of printing time onto the logger
logger = TimestampDecorator(logger)
printTimeSensitiveTestMessages(logger)

''' Another Example '''
def log_calls(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} called with args={args}, kwargs={kwargs} → returned {result}")
        return result
    return wrapper

# Example usage
def add(a, b):
    return a + b

print(add(1, 1))
add = log_calls(add)
print(add(2, 2))

# decorators are built in
@log_calls
def subtract(a, b):
    return a - b

subtract(3, 2)