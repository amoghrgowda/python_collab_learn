from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class TaskTemplate(ABC):
    """Abstract class defining a structured workflow for completing tasks."""

    def __init__(self, task_name):
        self.task_name = task_name
        self.completed = False

    def complete_task(self):
        """Template method defining the structured workflow for completing tasks."""
        print(f"Task '{self.task_name}' marked as completed.")
        self.completed = True
        self.after_complete()  # Optional behavior for specific task types

    def after_complete(self):
        """Hook method (optional behavior after marking as complete)."""
        pass

class RegularTask(TaskTemplate):
    """A simple task that can always be completed."""
    pass  # Uses the default template behavior

class DeadlineTask(TaskTemplate):
    """A task with a deadline that warns if it's overdue."""

    def __init__(self, task_name, due_date):
        super().__init__(task_name)
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")

    def after_complete(self):
        """Warns the user that the task was completed late"""
        if datetime.now() > self.due_date:
            print(f"Warning: Task '{self.task_name}' was overdue! (Deadline was {self.due_date.strftime('%Y-%m-%d')})")

class RecurringTask(TaskTemplate):
    """A task that generates a new instance when completed."""

    def __init__(self, task_name, interval_days):
        super().__init__(task_name)
        self.interval_days = interval_days
        self.completed_count = 0

    def after_complete(self):
        """Simulates scheduling the next occurrence of the task."""
        # get the day 7 days from now
        new_date = datetime.now() + timedelta(days=7)
        new_date = new_date.strftime('%Y-%m-%d')
        self.completed_count += 1
        print(f"Task {self.task_name} was completed {self.completed_count} times as of {datetime.now().strftime('%Y-%m-%d')}.")
        print(f"Setting Task {self.task_name} to be due on {new_date}.")
        


task1 = RegularTask("Buy groceries")
task2 = DeadlineTask("Submit tax forms", "2025-03-10")
task3 = RecurringTask("Water the plants", 7)

print("\nCompleting Regular Task:")
task1.complete_task()

print("\nCompleting Deadline Task:")
task2.complete_task()

print("\nCompleting Recurring Task:")
task3.complete_task()
task3.complete_task()  
