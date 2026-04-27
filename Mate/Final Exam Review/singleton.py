'''
Singleton

Def: The Singleton pattern restricts the instantiation of a class to ensure that only one instance of the class can be created and provides a global point of access to that instance.

When to use:
    1. Service locator / registry - Central registry of services or components looked up by name.
    2. Global Config - Application-wide settings loaded once and accessed everywhere.
    3. Shared Resource Mgt - One instance coordinates access to a shared resource.

'''

import time
class ExpensiveDatabaseConnection:
    _instance = None

    '''
    👉 __new__ → creates the object (allocates memory)
    👉 Singleton logic must live in __new__, because that’s where object creation is controlled.
    👉 super().__new__(cls) bypasses your override and uses the real object creator.
    👉 cls is the class itself (ExpensiveDatabaseConnection)
    '''
    def __new__(cls, *args, **kwargs):
        if cls._instance is None: # “Has an instance of this class already been created?”
            cls._instance = super().__new__(cls) # calls Python’s default object-creation logic; It allocates memory and returns a new instance
        return cls._instance

    '''
    👉 __init__ → initializes the object (sets up attributes)
    '''
    def _initialize(self):
        """Initialize the expensive database connection here."""
        time.sleep(1)
        print(f"Database connected")

# Usage:
db1 = ExpensiveDatabaseConnection() # db1 refers to that object ✅
db2 = ExpensiveDatabaseConnection() # db2 points to the same object ✅
db3 = ExpensiveDatabaseConnection() # db3 points to the same object ✅

# singletons avoid multiple instantiations of the same class, e.g. loggers
print(db1 is db2)  # True, both variables point to the same instance
print(db1 is db3)  # True, both variables point to the same instance
'''
Explaination: 
The program prints True because Python imports each module only once. 
Both db_connection and dbc reference the same module object, so db_instance refers to the same singleton instance in both cases.
'''

# in a different file, db_connection.py

# db_connection.py (module)
class _ExpensiveDatabaseConnection:
    def __init__(self):
        print(f"Database connected")

# Create a single instance at module level
db_instance = _ExpensiveDatabaseConnection()

# import db_connection

# db1 = db_connection.db_instance
# db2 = db_connection.db_instance

# print(db1 is db2)
# this prints true

# import db_connection
# db1 = db_connection.db_instance

# import db_connection as dbc
# db2 = dbc.db_instance
# print(db1 is db2)
'''
Explaination: 
    >> The program prints True because Python imports each module only once. 
    >> Both db_connection and dbc reference the same module object, so db_instance refers to the same singleton instance in both cases.

Why even do the Singleton Pattern if the module singleton gives true?
    >> Although Python modules behave like singletons, the Singleton pattern is still useful to explicitly control instantiation, enable lazy initialization, support subclassing, and express intent independently of the import system.
'''