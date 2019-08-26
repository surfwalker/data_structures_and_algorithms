from binary_tree import BinaryTree
from node import Node
from fizz_buzz_tree import fizz_buzz_tree
import pytest

def test_Node_class_exists():
    assert Node

def test_Node_instantiation():
    assert Node('value')

def test_BinaryTree_class_exists():
    assert BinaryTree

def test_BinaryTree_instantiation():
    assert BinaryTree()

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

def test_fizz_buzz():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)
    bt = BinaryTree()
    bt.root = one
    one.left_child = two
    one.right_child = three
    two.left_child = four
    two.right_child = five
    three.left_child = six
    three.right_child = seven
    four.left_child = eight
    four.right_child = nine
    five.left_child = ten
    five.right_child = eleven
    six.left_child = twelve
    six.right_child = thirteen
    seven.left_child = fourteen
    seven.right_child = fifteen
    fizz_buzz_tree(bt)
    assert bt.root.right_child.value is 'Fizz'

# # testing the whole tree
# def test__buzz(tree_fizz):
#     fizz_buzz_tree(tree_fizz)
#     assert tree_fizz.root.value is 'Fizz'
#     assert tree_fizz.root.left_child.value is 'Buzz'
#     assert tree_fizz.root.right_child.value is 'Fizz'
#     assert tree_fizz.root.left_child.right_child.value is 'Buzz'
#     assert tree_fizz.root.left_child.left_child.value is 'Fizz'
#     assert tree_fizz.root.right_child.right_child.value is 'FizzBuzz'
#     assert tree_fizz.root.right_child.left_child.value is 'Fizz'