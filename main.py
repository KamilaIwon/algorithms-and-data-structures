from drzewo_binarne import BinaryTree
from drzewo_binary_search import BinarySearchTree
from graf import Graph
from graf_wezel import Vertex
from g_path import GraphPath

'''
drzewo binarne
tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
tree.traverse_in_order(print)
print('----------')
tree.traverse_post_order(print)
print('----------')
tree.traverse_pre_order(print)
tree.show()

drzewo BST

binaryTree = BinarySearchTree(8)
binaryTree.insert(3)
binaryTree.insert(10)
binaryTree.insert_list([1, 6, 4, 7, 14, 13])
binaryTree.insert(2)
binaryTree.insert(25)
binaryTree.insert(30)
print(binaryTree.contains(60))
binaryTree.show()
print(binaryTree.find_parent(35))

GRAF
'''
# tworzymy instancję klasy Graph
g = Graph()

# tworzymy wierzchołki
a = g.create_vertex('A')
b = g.create_vertex('B')
c = g.create_vertex('C')
d = g.create_vertex('D')
e = g.create_vertex('E')
f = g.create_vertex('F')

# dodajemy krawędzie skierowane
g.add_undirected_edge(a, b, 6)
g.add_undirected_edge(a, d, 1)
g.add_undirected_edge(b, d, 2)
g.add_undirected_edge(b, e, 2)
g.add_undirected_edge(c, e, 5)
g.add_undirected_edge(c, b, 5)
g.add_undirected_edge(d, e, 1)

graf2 = Graph()
h = graf2.create_vertex(1)
i = graf2.create_vertex(2)
j = graf2.create_vertex(3)
k = graf2.create_vertex(4)
l = graf2.create_vertex(5)
graf2.add_directed_edge(h, j)
graf2.add_directed_edge(j, k)
graf2.add_directed_edge(k, l)
graf2.add_directed_edge(l, j)
graf2.add_directed_edge(i, l)
graf2.add_directed_edge(i, k)
graf2.add_directed_edge(h, i)
graf2.show()



# testujemy metodę traverse_depth_first
print('Przechodzenie w głąb:')
g.traverse_depth_first(print)
print('\nPrzechodzenie wszerz:')
g.traverse_breadth_first(print)

#g.show()
sciezka = GraphPath(g, a, c)
print(sciezka.draw_path())
print(GraphPath(graf2, h, l).draw_path())



