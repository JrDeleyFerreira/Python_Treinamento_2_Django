from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

# ------------------>> Classe de Iteração <<------------------
class MyIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0
        
    def __next__(self) -> Any:
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

# ------------------>> Classe Iterável <<------------------
class MyListIterable(Iterable):
    def __init__(self) -> None:
        self._itens: List[Any] = []
        
    def add(self, value: Any) -> None:
        self._itens.append(value)
        
    def __iter__(self) -> MyIterator:
        return MyIterator(self._itens)

# ------------------>> Como usar <<------------------
if __name__ == '__main__':
    ...