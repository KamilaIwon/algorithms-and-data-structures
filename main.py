from drzewo_binarne import BinaryTree
from drzewo_binary_search import BinarySearchTree

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
'''
binaryTree = BinarySearchTree(8)
binaryTree.insert(3)
binaryTree.insert(10)
binaryTree.insert_list([1, 6, 4, 7, 14, 13])
binaryTree.insert(2)
binaryTree.insert(25)
binaryTree.insert(30)




binaryTree.show()
