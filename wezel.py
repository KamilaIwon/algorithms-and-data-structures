from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self,
                 value: Any = None,
                 next: 'Node' = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f'{self.value}'
