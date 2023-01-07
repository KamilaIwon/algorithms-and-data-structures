from graphviz import graphs
from typing import Any, List, Callable, Union
from kolejka import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self,
                 value: Any = None,
                 children=None):
        if children is None:
            children = []
        self.value = value
        self.children = children

    def isleaf(self) -> bool:
        if self.children.__len__() == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def __repr__(self) -> str:
        return f'{self.value}'

    def for_each_deep_first(self,
                            visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self,
                             visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue = Queue()
        for child in self.children:
            queue.enqueue(child)
        while queue.__len__() != 0:
            element = queue.dequeue()
            visit(element)
            for child in element.children:
                queue.enqueue(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for child in self.children:
            if child.value == value:
                return child
        return None
