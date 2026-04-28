# db_connection.py (module)
class _ExpensiveDatabaseConnection:
    def __init__(self):
        print(f"Database connected")

# Create a single instance at module level
db_instance = _ExpensiveDatabaseConnection()