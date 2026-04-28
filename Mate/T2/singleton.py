# rewrite the above into
import time
class ExpensiveDatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # cls._instance._initialized = False
        return cls._instance

    def _initialize(self):
        """Initialize the expensive database connection here."""
        time.sleep(1)
        print(f"Database connected")

# Usage:
db1 = ExpensiveDatabaseConnection()
db2 = ExpensiveDatabaseConnection()
db3 = ExpensiveDatabaseConnection()

# singletons avoid multiple instantiations of the same class, e.g. loggers
print(db1 is db2)  # True, both variables point to the same instance
print(db1 is db3)  # True, both variables point to the same instance

# in a different file, db_connection.py

import db_connection

db1 = db_connection.db_instance
db2 = db_connection.db_instance

print(db1 is db2)