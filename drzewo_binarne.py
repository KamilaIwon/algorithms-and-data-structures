from drzewo_binarne_wezel import BinaryNode
from typing import Any, Callable
from graphviz import Digraph


class BinaryTree:
    root: 'BinaryNode'

    def __init__(self, value: Any = None) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def show(self):
        tree = Digraph(format='png')

        def edges(element: 'BinaryNode') -> None:
            if element.left_child:
                tree.edge(str(element.value), str(element.left_child.value))
                edges(element.left_child)
            if element.right_child:
                tree.edge(str(element.value), str(element.right_child.value))
                edges(element.right_child)

        tree.node(str(self.root.value))
        edges(self.root)

        tree.view()





