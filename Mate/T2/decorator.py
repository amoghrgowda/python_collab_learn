'''
- dynamically add behaviors to objects
- add behavior to objects not necessarily related to each other
- implemented a single time then attach decorator to multiple classes
- careful in managing decorators, can get clunky
'''

import time

class Printer:
  def print(self, text):
    print(f"[LOG] {text}")

class DatePrefixPrinter:
    def __init__(self, printer):
        self._printer = printer
    
    def print(self, text):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self._printer.print(f"{ts} - {text}")

def printTestMessages(printer):  
  printer.print("First Test message")
  printer.print("Second Test message")
  printer.print("Third Test message")

def printTimeSensitiveTestMessages(printer):

  printer.print("First Test message")

  time.sleep(1)
  printer.print( "Second Test message")

  time.sleep(1)
  printer.print( "Third Test message")

  time.sleep(1)
  printer.print( "Fourth test message")

logger = Printer()
printTestMessages(logger)

# we can add the additional behavior of printing time onto the logger
logger = DatePrefixPrinter(logger)
printTimeSensitiveTestMessages(logger)