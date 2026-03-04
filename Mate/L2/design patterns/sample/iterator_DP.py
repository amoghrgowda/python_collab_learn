from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self): ...

    @abstractmethod
    def next(self): ...

class CIterator(Iterator):
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            value = self.collection[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        pass

class CAggregate(Aggregate):
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)

    def create_iterator(self):
        return CIterator(self.data)

# Example Usage:
aggregate = CAggregate()
aggregate.add_item(1)
aggregate.add_item(2)
aggregate.add_item(3)
iterator = aggregate.create_iterator()
while iterator.has_next():
    print(iterator.next())
# Output:
# 1
# 2
# 3