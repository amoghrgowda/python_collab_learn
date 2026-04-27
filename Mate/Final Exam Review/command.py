from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self): pass
    @abstractmethod
    def undo(self): pass

class TodoList:
    def __init__(self): self.tasks = []
    def add_task(self, task): self.tasks.append(task); print(f"Added: {task}")
    def remove_task(self, task): self.tasks.remove(task); print(f"Removed: {task}")
    def show_tasks(self): print("Tasks:", self.tasks)

class AddTaskCommand(Command):
    def __init__(self, todo, task): self.todo, self.task = todo, task
    def execute(self): self.todo.add_task(self.task)
    def undo(self): self.todo.remove_task(self.task)

class RemoveTaskCommand(Command):
    def __init__(self, todo, task): self.todo, self.task = todo, task
    def execute(self): self.todo.remove_task(self.task)
    def undo(self): self.todo.add_task(self.task)

class CommandInvoker:
    def __init__(self): self.history = []
    def execute(self, command): command.execute(); self.history.append(command)
    def undo(self):
        if self.history: 
            command_to_undo = self.history.pop()  # Get the last executed command
            command_to_undo.undo()  # Call undo on it
        else: 
            print("Nothing to undo.")

# Usage
todo = TodoList()
invoker = CommandInvoker()
add_cmd = AddTaskCommand(todo, "Buy milk")

invoker.execute(add_cmd)
todo.show_tasks()
invoker.undo()
todo.show_tasks()
