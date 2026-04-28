from datetime import datetime


class UserDataPrinter:
    def display(self):
      print(f"User: {self.name}, Age: {self.age}, City: {self.city}")


class UserData(UserDataPrinter):
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
    def display(self):
        return super().display()


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

# Adapter: Converts ExternalJSONData to match the UserDataPrinter class.
class JSONToUserAdapter(UserDataPrinter):
    def __init__(self, external_json_data: ExternalJSONData):
        json_data = external_json_data.get_data()
        
        self.external_json_data = external_json_data
        self.name = json_data["full_name"]
        # self.age = 2026 - json_data["details"]["year_born"]  # Calculate age from year_born
        self.age = datetime.now().year - json_data["details"]["year_born"]  # Calculate age from year_born
        self.city = json_data["details"]["location"]
  
    def display(self):
        return super().display()


if __name__ == "__main__":
    print("Using Native UserData:")
    user1 = UserData("Bob", 25, "New York")
    user1.display()

    print("\nUsing Adapted Data:")
    external_data = ExternalJSONData()
    adapted_user = JSONToUserAdapter(external_data)
    adapted_user.display()
