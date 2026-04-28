from abc import ABC, abstractmethod

class TaskComponent(ABC):
    @abstractmethod
    def show(self, indent=0):
        pass

class Task(TaskComponent):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print(' ', indent, f'[] {self.name}')

# Composite: A task group that can hold multiple tasks (including subtasks)
class TaskGroup(TaskComponent):
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add(self, task: TaskComponent):
        self.tasks.append(task)

    def remove(self, task: TaskComponent):
        self.tasks.remove(task)

    def show(self, indent=0):
        print(' ', indent, f'[] {self.name}')
        for task in self.tasks:
            task.show(indent + 1)

if __name__ == "__main__":

    project = TaskGroup("Week 4 Plan")

    task1 = Task("Buy more groceries")
    task2 = Task("Pay rent")

    project.add(task1)
    project.add(task2)

    coding_tasks = TaskGroup("Tutorial Tasks")
    coding_tasks.add(Task("Fix bug #123"))
    coding_tasks.add(Task("Refactor composite pattern"))

    project.add(coding_tasks)

    project.show()
