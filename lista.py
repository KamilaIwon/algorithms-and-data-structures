from typing import Any, Type
from wezel import Node


class LinkedList:
    head: 'Node'
    tail: 'Node'

    def __init__(self,
                 head: Node = None,
                 tail: Node = None):
        self.head = head
        self.tail = tail

    def __len__(self):
        tmp = self.head
        length = 0
        while tmp is not None:
            length += 1
            tmp = tmp.next
        return length

    def push(self, value: Any) -> None:
        new = Node(value)
        if len(self) == 0:
            self.head = new
            self.tail = new
            return

        new.next = self.head
        self.head = new

    def __repr__(self) -> str:
        if self.head is None:
            return f'list is empty'
        result = f''
        tmp = self.head
        while tmp.next is not None:
            result += f'{tmp.value} -> '
            tmp = tmp.next
        result += f'{tmp.value}'
        return result

    def append(self, value: Any) -> None:
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
            return

        self.tail.next = new
        self.tail = new

    def insert(self, value: Any, after: Node) -> None:
        tmp = self.head
        new = Node(value)
        while tmp != after:
            if tmp is None:
                return
            tmp = tmp.next

        if after is self.tail:
            self.tail = new
        new.next = after.next
        after.next = new

    def node(self, at: int) -> Node:
        if at >= self.__len__():
            print(f'list isn\'t that long')
            return None
        if at < 0:
            print('wrong number')
            return None
        where = 0
        tmp = self.head
        while where != at:
            where += 1
            tmp = tmp.next
        return tmp

    def pop(self) -> Any:

        if self.head is None:
            return None

        if len(self) == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp.value

        tmp = self.head
        self.head = self.head.next
        return tmp.value

    def remove_last(self) -> Any:
        if self.head is None:
            return None
        if len(self) == 1:
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp.value
        tmp = self.head
        while tmp.next is not self.tail:
            tmp = tmp.next
        result = self.tail
        tmp.next = None
        self.tail = tmp
        return result.value

    def remove(self, after: 'Node') -> Any:
        if after is self.tail:
            return f'node doesn\'t exist :('
        if after is None:
            return f'list is empty'
        tmp = after.next
        after.next = after.next.next
        if len(self) == 1:
            self.tail = self.head
        return tmp
