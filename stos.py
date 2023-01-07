from lista import LinkedList
from typing import Any


class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.__len__()

    def __str__(self) -> str:
        result = f''
        if self.__len__() == 0:
            return 'stack is empty'
        tmp = self._storage.head
        while tmp is not None:
            result += f'\n{tmp.value}'
            tmp = tmp.next
        return result

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()
