from lista import LinkedList
from typing import Any


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return self._storage.__len__()

    def __str__(self) -> str:
        result = f''
        if self.__len__() == 0:
            return f'this queue is empty :('
        tmp = self._storage.head
        while tmp.next is not None:
            result += f'{tmp.value}, '
            tmp = tmp.next
        result += f'{tmp.value}'
        return result

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()
