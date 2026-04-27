import datetime

class UserDataPrinter:
    def display(self):
      print(f"User: {self.name}, Age: {self.age}, City: {self.city}") # type: ignore

class UserData(UserDataPrinter):
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
    def display(self):
        return super().display() # “Give me access to the parent class of the current class.”

# Data Source 2: Has the same data but in a different format (JSON-like dict).
class ExternalJSONData:
    def __init__(self):
        self.data = {
            "full_name": "Alice Smith",
            "details": {
                "year_born": 1995,
                "location": "Sydney"
            }
        }

    def get_data(self):
        return self.data

'''
Because the data from ExternalJSONData doesn't fit into the UserDataPrinter, we had to manually do some work to convert them. The conversion can be complex, and would be more maintainable if we move its complexity into a class. 

Instead, let's use an adapter. Fill in the ??? hole
'''
# Adapter: Converts ExternalJSONData to match the UserDataPrinter class.
class JSONToUserAdapter(UserDataPrinter):
    def __init__(self, external_json_data: ExternalJSONData):
        json_data = external_json_data.get_data()
        
        print(f">>> {json_data}")
        self.name = json_data["full_name"] # type: ignore

        year_now = datetime.date.today().year
        year_born = json_data["details"]["year_born"]
        self.age = year_now - year_born 

        self.city = json_data["details"]["location"]
  
    def display(self):
        return super().display() # “Give me access to the parent class of the current class.”


if __name__ == "__main__":
    print("Using Native UserData:")
    user1 = UserData("Bob", 25, "New York")
    user1.display()

    print("\nUsing Adapted Data:")
    external_data = ExternalJSONData()
    adapted_user = JSONToUserAdapter(external_data)
    adapted_user.display()
