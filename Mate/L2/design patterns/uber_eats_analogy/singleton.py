'''
Singleton Pattern: Ensures a class has only one instance and provides a global point of access to it.

This is the single source of truth for API keys, user region, currency, feature flags, logging settings, rate limits, environment (dev/staging/prod), etc.), etc. that all parts of the application can access and modify as needed.
'''

class UberEatsConfig:
    _instance = None
    _initialized = False # prevents re-running __init__

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Prevent __init__ from running more than once if not self._initialized:
        if not self._initialized:
            self.api_key = "DEFAULT_KEY"
            self.region = "Sydney"
            self.currency = "AUD"
            self.feature_flags = {"dark_mode": True}
            self.rate_limits = {"requests_per_minute": 1000}
            UberEatsConfig._initialized = True

# Example Usage:
c1 = UberEatsConfig()
c2 = UberEatsConfig()

c1.api_key = "XYZ-123"

print(c2.api_key)      # XYZ-123
print(c1 is c2)        # True
