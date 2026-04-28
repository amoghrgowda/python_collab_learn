
"""
Iterator Pattern Example: Menu iteration with custom filtering
----------------------------------------------------------------
- Provides a uniform way to traverse different collections without exposing internals.
- Here we implement a Menu (aggregate) that can produce different iterators:
  * FullMenuIterator: iterate every item
  * VegetarianIterator: iterate only vegetarian items
  * PriceCappedIterator: iterate items up to a given price

How this helps:
- You can add new traversal strategies (iterators) without changing the Menu class.
- Client code can swap iterators as needed (Open/Closed principle).

Usage:
    from iterator import Menu, VegetarianIterator

    menu = Menu([
        {"name": "Margherita Pizza", "price": 12.5, "vegetarian": True},
        {"name": "BBQ Chicken Pizza", "price": 15.0, "vegetarian": False},
        {"name": "Penne Arrabiata", "price": 13.0, "vegetarian": True},
    ])

    for item in VegetarianIterator(menu):
        print(item["name"])  # Margherita Pizza, Penne Arrabiata
"""
from __future__ import annotations
from typing import Iterable, Iterator, List, Dict, Any

MenuItem = Dict[str, Any]

class Menu:
    def __init__(self, items: Iterable[MenuItem]):
        self._items: List[MenuItem] = list(items)

    def __iter__(self) -> Iterator[MenuItem]:
        return FullMenuIterator(self)

    @property
    def items(self) -> List[MenuItem]:
        # Expose a read-only like view (copy) to prevent external mutation
        return list(self._items)

class FullMenuIterator:
    def __init__(self, menu: Menu):
        self._menu = menu
        self._index = 0

    def __iter__(self) -> 'FullMenuIterator':
        return self

    def __next__(self) -> MenuItem:
        if self._index >= len(self._menu._items):
            raise StopIteration
        item = self._menu._items[self._index]
        self._index += 1
        return item

class VegetarianIterator:
    def __init__(self, menu: Menu):
        self._filtered = [i for i in menu.items if i.get("vegetarian")]
        self._index = 0

    def __iter__(self) -> 'VegetarianIterator':
        return self

    def __next__(self) -> MenuItem:
        if self._index >= len(self._filtered):
            raise StopIteration
        item = self._filtered[self._index]
        self._index += 1
        return item

class PriceCappedIterator:
    def __init__(self, menu: Menu, max_price: float):
        self._filtered = [i for i in menu.items if float(i.get("price", 0)) <= max_price]
        self._index = 0

    def __iter__(self) -> 'PriceCappedIterator':
        return self

    def __next__(self) -> MenuItem:
        if self._index >= len(self._filtered):
            raise StopIteration
        item = self._filtered[self._index]
        self._index += 1
        return item

if __name__ == "__main__":
    menu = Menu([
        {"name": "Margherita Pizza", "price": 12.5, "vegetarian": True},
        {"name": "BBQ Chicken Pizza", "price": 15.0, "vegetarian": False},
        {"name": "Penne Arrabiata", "price": 13.0, "vegetarian": True},
    ])
    print("-- Full Menu --")
    for item in menu:
        print(item["name"])

    print("
-- Vegetarian --")
    for item in VegetarianIterator(menu):
        print(item["name"])

    print("
-- <= $13 --")
    for item in PriceCappedIterator(menu, 13.0):
        print(item["name"])
