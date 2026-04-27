'''
Exercise: Refactor this code to use the Strategy pattern. In particular, we would like to make it easy to implement new methods of sorting the code. A partially completed answer is provided below, where you have to fill in the holes (indicated with "??? TODO").
'''

from typing import List
from abc import ABC, abstractmethod

class Task:
    def __init__(self, title: str, priority: int, due_date: str, created_at: str, completed: bool):
        self.title = title
        self.priority = priority
        self.due_date = due_date  # Format: YYYY-MM-DD
        self.created_at = created_at  # Format: YYYY-MM-DD
        self.completed = completed

    def __repr__(self):
        return f"{self.title} (Priority: {self.priority}, Due: {self.due_date}, Created: {self.created_at}, Completed: {self.completed})"


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, tasks: List[Task]) -> List[Task]:
        pass


class SortByDueDate(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.due_date)


class SortByPriority(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.priority, reverse=True)


class SortByCreationTime(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.created_at)


class SortByCompletionStatus(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.completed)


class ToDoList:
    def __init__(self, strategy: SortingStrategy):
        self.tasks = []
        self.strategy = strategy

    def add_task(self, task: Task):
        self.tasks.append(task)

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def show_tasks(self):
        sorted_tasks = self.strategy.sort(self.tasks)
        for task in sorted_tasks:
            print(task)


if __name__ == "__main__":
    tasks = [
        Task("Buy groceries", 2, "2025-03-12", "2025-03-17", False),
        Task("Complete tutorial", 1, "2025-03-10", "2025-03-17", False),
        Task("Pay rent", 3, "2025-03-15", "2025-03-05", True),
        Task("Book a flight", 1, "2025-03-11", "2025-03-06", False),
    ]

    todo_list = ToDoList(SortByDueDate())  

    for task in tasks:
        todo_list.add_task(task)

    print("Tasks sorted by Due Date:")
    todo_list.show_tasks()

    print("\nSwitching to sorting by Priority:")
    todo_list.set_strategy(SortByPriority())
    todo_list.show_tasks()

    print("\nSwitching to sorting by Creation Time:")
    todo_list.set_strategy(SortByCreationTime())
    todo_list.show_tasks()

    print("\nSwitching to sorting by Completion Status:")
    todo_list.set_strategy(SortByCompletionStatus())
    todo_list.show_tasks()
