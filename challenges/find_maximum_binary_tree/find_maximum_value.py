from binary_tree import BinaryTree
from collections import deque
from node import Node

def find_maximum_value(binary_tree):
    if not binary_tree.root:
        return "This binary tree is empty."
    else:
        maximum_value_queue = deque()
        maximum_value = binary_tree.root.value
        maximum_value_queue.appendleft(binary_tree.root)
        while len(maximum_value_queue):
            current_node = maximum_value_queue.pop()
            if current_node.value > maximum_value:
                maximum_value = current_node.value
            if current_node.left_child:
                maximum_value_queue.appendleft(current_node.left_child)
            if current_node.right_child:
                maximum_value_queue.appendleft(current_node.right_child)
        return maximum_value