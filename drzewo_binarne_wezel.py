from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,
                 value: Any = None,
                 left_child: 'BinaryNode' = None,
                 right_child: 'BinaryNode' = None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def is_leaf(self):
        if self.right_child or self.left_child:
            return False
        return True

    def add_left_child(self, value: Any) -> 'BinaryNode':
        new = BinaryNode(value)
        self.left_child = new
        return new

    def add_right_child(self, value: Any) -> 'BinaryNode':
        new = BinaryNode(value)
        self.right_child = new
        return new

    def __repr__(self) -> str:
        return f'{self.value}'

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

