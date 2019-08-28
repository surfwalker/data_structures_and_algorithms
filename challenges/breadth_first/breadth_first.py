from binary_tree import BinaryTree
from collections import deque
from node import Node

def breadth_first(binary_tree):
    if not binary_tree.root:
        return "This binary tree is empty."
    else:
        breadth_results = []
        breadth_queue = deque()
        breadth_queue.appendleft(binary_tree.root)
        while len(breadth_queue):
            node = breadth_queue.pop()
            breadth_results.append(node.value)
            if node.left_child:
                breadth_queue.appendleft(node.left_child)
            if node.right_child:
                breadth_queue.appendleft(node.right_child)
        return breadth_results