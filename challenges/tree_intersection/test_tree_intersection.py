from binary_search_tree import BinarySearchTree
from binary_tree import BinaryTree
from node import Node
from tree_intersection import tree_intersection
import pytest

@pytest.fixture()
def bt_1():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    bt = BinaryTree()
    bt.root = one
    return bt

@pytest.fixture()
def bt_2():
    one = Node(2)
    two = Node(4)
    three = Node(6)
    four = Node(8)
    five = Node(10)
    six = Node(12)
    seven = Node(3)
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    bt = BinaryTree()
    bt.root = one
    return bt    
    
def test_Node_exists():
    assert Node

def test_Node_instantiation():
    assert Node('value')

def test_BinaryTree_exists():
    assert BinaryTree

def test_BinaryTree_instantiation():
    assert BinaryTree()

def test_BinarySearchTree_exists():
    assert BinarySearchTree

def test_BinarySearchTree_instantiation():
    assert BinarySearchTree()

def test_tree_intersection_exists():
    assert tree_intersection

def test_tree_intersection_with_one_matching_value():
    one = Node(7)
    two = Node(7)
    bt_1 = BinaryTree()
    bt_2 = BinaryTree()
    bt_1.root = one
    bt_2.root = two
    assert tree_intersection(bt_1, bt_2) == [7]

def test_tree_intersection_with_many_matching_values(bt_1, bt_2):
    assert tree_intersection(bt_1, bt_2) == [4, 2, 6, 3]

def test_tree_intersection_with_no_matching_values():
    one = Node(7)
    two = Node(777)
    bt_1 = BinaryTree()
    bt_2 = BinaryTree()
    bt_1.root = one
    bt_2.root = two
    assert tree_intersection(bt_1, bt_2) == "There are no matching values."