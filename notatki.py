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
        if value < node.value:
            if node.left_child:
                self._insert(node.left_child, value)
            if node.left_child is None:
                node.left_child = BinaryNode(value)
        if value > node.value:
            if node.right_child:
                self._insert(node.right_child, value)
            if node.right_child is None:
                node.right_child = BinaryNode(value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for value in list_:
            self._insert(self.root, value)

    def contains(self, value: Any) -> bool:
        element = self.root

        while element is not None:
            if element.value == value:
                return True
            if value > element.value:
                if element.right_child is None:
                    return False
                element = element.right_child
            if value < element.value:
                if element.left_child is None:
                    return False
                element = element.left_child
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def find_parent(self, value: Any) -> BinaryNode:
        def find(element: 'BinaryNode') -> 'BinaryNode':
            if value < element.value:
                if element.left_child.value == value:
                    return element
                if element.left_child is None:
                    return None
                return find(element.left_child)

            if value > element.value:
                if element.right_child.value == value:
                    return element
                if element.right_child is None:
                    return None
                return find(element.right_child)

        return find(self.root)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        # metoda ktora znajduje wybrany do usuniecia wezel
        def find(element: 'BinaryNode'):
            if value < element.value:
                if element.left_child is None:
                    return None
                if element.left_child.value == value:
                    return element.left_child
                else:
                    return find(element.left_child)
            if value > element.value:
                if element.right_child is None:
                    return None
                if element.right_child.value == value:
                    return element.right_child
                else:
                    return find(element.right_child)
            if value == element.value:
                return element

        found = find(node)

        # gdy usuwany node ma 0 dzieci, jest lisciem
        if found.is_leaf():
            if found == self.root:
                self.root = None
                return self.root
            parent = self.find_parent(found.value)
            if parent.left_child:
                if parent.left_child.value == found.value:
                    parent.left_child = None
            if parent.right_child:
                if parent.right_child.value == found.value:
                    parent.right_child = None

        # gdy usuwany node ma dwojke dzieci
        if found.left_child and found.right_child:
            # znajdz zastepstwo: najdalej wysoniety na lewo node od str prawego dziecka
            replacement = found.right_child.min()

            # znajdz rodzica zastepstwa
            old_parent = self.find_parent(replacement.value)
            if old_parent.left_child == replacement:
                old_parent.left_child = replacement.right_child
            else:
                old_parent.right_child = replacement.right_child
            # zamien dzieci
            replacement.right_child = found.right_child
            replacement.left_child = found.left_child
            found.value = replacement.value
            # usun zastepstwo
            replacement = None
            return self.root

        # usuwany node ma tylko 1 dziecko
        if found.right_child is None and found.left_child \
                or found.right_child and found.left_child is None:
            if found is self.root:
                if found.right_child:
                    self.root = found.right_child
                else:
                    self.root = found.left_child
                return self.root
            parent = self.find_parent(found.value)
            if found.right_child:
                child = found.right_child
            else:
                child = found.left_child

            if parent.left_child:
                if parent.left_child.value == found.value:
                    parent.left_child = child
            if parent.right_child:
                if parent.right_child.value == found.value:
                    parent.right_child = child


        return self.root

    '''
    idk ktora wersja usuwania node z 2 dziecmi jest poprawna
            if found.left_child and found.right_child:
            replacement = found.left_child.max()
            old_parent = self.find_parent(replacement.value)
            if old_parent.left_child:
                if old_parent.left_child.value == replacement.value:
                    old_parent.left_child = None
            if old_parent.right_child:
                if old_parent.right_child.value == replacement.value:
                    old_parent.right_child = None
            replacement.right_child = found.right_child
            replacement.left_child = found.left_child
            found.value = replacement.value
            replacement = None
            return self.root
    '''
