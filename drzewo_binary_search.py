from drzewo_binary_search_wezel import BinaryNode
from typing import Any, List
from graphviz import Digraph


class BinarySearchTree:
    root: 'BinaryNode'

    def __init__(self, value: Any = None):
        self.root = BinaryNode(value)

    def show(self) -> None:

        tree = Digraph(format='png')

        def edges(element: 'BinaryNode') -> None:
            if element.left_child:
                tree.edge(str(element.value), str(element.left_child.value))
                edges(element.left_child)
            if element.right_child:
                tree.edge(str(element.value), str(element.right_child.value))
                edges(element.right_child)

        if self.root:
            tree.node(str(self.root.value))
            edges(self.root)
        tree.view()

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is not None:
            if value < node.value:
                if node.left_child:
                    self._insert(node.left_child, value)
                else:
                    node.left_child = BinaryNode(value)
            if value > node.value:
                if node.right_child:
                    self._insert(node.right_child, value)
                else:
                    node.right_child = BinaryNode(value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for value in list_:
            self._insert(self.root, value)

    def remove(self, value: Any):
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any):
        if node is not None:
            if value == node.value:
                if node.right_child is None and node.left_child is None:
                    return None
                elif node.left_child is None:
                    return node.right_child
                elif node.right_child is None:
                    return node.left_child
                node.value = node.right_child.min().value
                node.right_child = self._remove(node.right_child, node.value)

            elif value < node.value:
                node.left_child = self._remove(node.left_child, value)
            else:
                node.right_child = self._remove(node.right_child, value)
        return node

    def contains(self, value: Any):
        if self._contains(self.root, value):
            return True
        return False

    def _contains(self, node: 'BinaryNode', value: Any) -> 'BinaryNode':

        if node is not None:
            if value == node.value:
                return node
            elif value > node.value:
                return self._contains(node.right_child, value)
            else:
                return self._contains(node.left_child, value)
        return node
