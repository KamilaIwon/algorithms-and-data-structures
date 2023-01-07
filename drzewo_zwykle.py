from drzewo_zwykle_wezel import TreeNode
from typing import Any, Callable
from kolejka import Queue
from graphviz import Digraph


class Tree:
    root: 'TreeNode'

    def __init__(self, root: 'TreeNode' = None):
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        queue = Queue()
        if self.root.value == parent_name:
            self.root.children.append(TreeNode(value))
            return
        for child in self.root.children:
            queue.enqueue(child)
        while queue.__len__() != 0:
            element = queue.dequeue()
            if element.value == parent_name:
                element.children.append(TreeNode(value))
                return
            for child in element.children:
                queue.enqueue(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def show(self):
        tree = Digraph(format='png')
        all_nodes = []
        queue = Queue()
        queue.enqueue(self.root)
        all_nodes.append(self.root)
        while queue.__len__() != 0:
            element = queue.dequeue()
            for child in element.children:
                all_nodes.append(child)
                queue.enqueue(child)

        visited = []
        for node in all_nodes:
            if node not in visited:
                visited.append(node)
                for child in node.children:
                    tree.edge(node.value, child.value)

        tree.view()


korzen = TreeNode('F')
korzen.add(TreeNode('B'))
korzen.add(TreeNode('G'))
drzewo = Tree(korzen)
drzewo.add('A', 'B')
drzewo.add('D', 'B')
drzewo.add('C', 'D')
drzewo.add('E', 'D')
drzewo.add('I', 'G')
drzewo.add('H', 'I')
drzewo.for_each_deep_first(print)
print('----')
drzewo.for_each_level_order(print)
print('----')
drzewo.show()
