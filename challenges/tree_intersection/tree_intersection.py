from binary_search_tree import BinarySearchTree
from binary_tree import BinaryTree
from node import Node

def tree_intersection(bt_1, bt_2):
    if bt_1.root == None or bt_2.root == None:
        return None
    matching_values = []
    def visit_node(node_one):
        if node_one.left_child:
            visit_node(node_one.left_child)
        evaluate_nodes(node_one, bt_2.root)
        if node_one.right_child:
            visit_node(node_one.right_child)
    def evaluate_nodes(node_1, node_2):
        if node_2.left_child:
            evaluate_nodes(node_1, node_2.left_child)
        if node_1.value == node_2.value:
            matching_values.append(node_1.value)
            return
        if node_2.right_child:
            evaluate_nodes(node_1, node_2.right_child)
    visit_node(bt_1.root)
    if matching_values:
        return matching_values
    else:
        return "There are no matching values."