from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any = None,
                 left_child: 'BinaryNode' = None,
                 right_child: 'BinaryNode' = None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def min(self) -> 'BinaryNode':
        min = self
        while min.left_child is not None:
            if min.left_child:
                min = min.left_child
        return min

    def max(self) -> 'BinaryNode':
        max = self
        while max.right_child is not None:
            if max.right_child:
                max = max.right_child
        return max

    def __repr__(self):
        return f'{self.value}'

    def is_leaf(self) -> bool:
        if self.left_child or self.right_child:
            return False
        return True

