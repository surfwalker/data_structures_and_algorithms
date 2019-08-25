from binary_tree import BinaryTree
from node import Node
from binary_search_tree import BinarySearchTree
import pytest

def test_BinaryTree_class_exists():
    assert BinaryTree

def test_BinaryTree_instantiation():
    assert BinaryTree()

def test_BinarySearchTree_class_exists():
    assert BinarySearchTree

def test_BinarySearchTree_instantiation():
    assert BinarySearchTree()

def test_bst_with_root_node():
    one = Node('pipeline')
    bt = BinaryTree()
    bt.root = one
    assert bt.root
    assert bt.root.value == 'pipeline'

def test_bst_add_node_single():
    bst = BinarySearchTree()
    bst.add('pipeline')
    assert bst.root.value == 'pipeline'

def test_bst_add_left_child_node():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(5)
    assert bst.root.value == 10
    assert bst.root.left_child.value == 5

def test_bst_add_right_child_node():
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(15)
    assert bst.root.value == 10
    assert bst.root.right_child.value == 15

def test_binary_tree_inorder_traversal():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    bt = BinaryTree()
    bt.root = one
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    expected = [4, 2, 5, 1, 6, 3, 7]
    actual = bt.in_order()
    assert actual == expected

def test_binary_tree_pre_order_traversal():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    bt = BinaryTree()
    bt.root = one
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    expected = [1, 2, 4, 5, 3, 6, 7]
    actual = bt.pre_order()
    assert actual == expected

def test_binary_tree_post_order_traversal():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    bt = BinaryTree()
    bt.root = one
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    expected = [4, 5, 2, 6, 7, 3, 1]
    actual = bt.post_order()
    assert actual == expected