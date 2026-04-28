from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, task):
        pass

# an observer that sends emails
class EmailNotifier(Observer):
    def update(self, task):
        print(f"📧 Email Notifier: Task '{task}' has been added.")

# an observer that logs additions
class Logger(Observer):
    def update(self, task):
        print(f"📝 Logger: Task '{task}' has been added.")

class TodoList:
    def __init__(self):
        self.tasks = []
        self.observers = []

    def attach(self, observer):
        # update self.observers
        # ??? TODO
        self.observers.append(observer)

    def notify(self, task):
        # call the observers
        # ??? TODO
        for observer in self.observers:
            observer.update(task)

    def add_task(self, task):
        self.tasks.append(task)
        self.notify(task)

if __name__ == "__main__":
    todo_list = TodoList()

    email_notifier = EmailNotifier()
    logger = Logger()

    # Attach observers
    todo_list.attach(email_notifier)
    todo_list.attach(logger)

    # Add a task
    todo_list.add_task("Complete SOFT3202 assignment")
