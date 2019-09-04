from node import Node
from binary_tree import BinaryTree
from find_maximum_value import find_maximum_value
import pytest

def test_Node_class_exists():
    assert Node

def test_Node_instantiation():
    assert Node('value')

def test_BinaryTree_class_exists():
    assert BinaryTree

def test_BinaryTree_instantiation():
    assert BinaryTree()

def test_find_maximum_value():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(10)
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
    expected = 10
    actual = find_maximum_value(bt)
    assert actual == expected

def test_find_maximum_value_tree_empty():
    bt = BinaryTree()
    expected = "This binary tree is empty."
    actual = find_maximum_value(bt)
    assert actual == expected