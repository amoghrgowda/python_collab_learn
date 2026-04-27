import csv
import json
import os

class CSVTaskStorage:
    """Handles storing tasks in a CSV file."""
    def __init__(self, filename):
        self.filename = filename
        self.headers = ["ID", "Task", "Status"]

        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def add_task(self, task_id, task):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([task_id, task, "Pending"])

    def get_tasks(self):
        with open(self.filename, "r", newline="") as file:
            return list(csv.reader(file))[1:]


class JSONMetadataStorage:
    """Stores additional metadata (e.g., due dates)."""
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump({}, file)

    def add_metadata(self, task_id, due_date):
        metadata = self.get_metadata()
        metadata[str(task_id)] = {"Due Date": due_date}

        with open(self.filename, "w") as file:
            json.dump(metadata, file, indent=4)

    def get_metadata(self):
        with open(self.filename, "r") as file:
            return json.load(file)


class StorageFacade:
    """Facade to simplify interactions with storage components."""
    def __init__(self, task_file="tasks.csv", metadata_file="metadata.json"):
        self.task_storage = CSVTaskStorage(task_file)
        self.metadata_storage = JSONMetadataStorage(metadata_file)

    def add_task(self, task_id, task, due_date):
        '''??? TODO'''
        self.task_storage.add_task(task_id, task)
        self.metadata_storage.add_metadata(task_id, due_date)
        

    def get_tasks_with_metadata(self):
        '''??? TODO'''
        tasks = self.task_storage.get_tasks()
        metadata = self.metadata_storage.get_metadata()
        return [(task_id, task, metadata.get(task_id, {}).get("Due Date", "N/A")) for task_id, task, _ in tasks]


class TaskManager:
    """Manages tasks and interacts with the storage facade."""
    def __init__(self):
        self.storage = StorageFacade()
        self.task_counter = 1

    def add_task(self, task, due_date):
        self.storage.add_task(self.task_counter, task, due_date)
        print(f"Added Task: [{self.task_counter}] {task} (Due: {due_date})")
        self.task_counter += 1

    def list_tasks(self):
        tasks = self.storage.get_tasks_with_metadata()
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for task_id, task, due_date in tasks:
                print(f"[{task_id}] {task} (Due: {due_date})")


if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Finish assignment", "2025-03-17")
    manager.add_task("Groceries", "2025-03-18")
    manager.list_tasks()