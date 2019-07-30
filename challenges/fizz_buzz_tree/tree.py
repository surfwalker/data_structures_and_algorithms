from node import Node

class BinaryTree:

    def __init__(self):
        self.root = None
        
    def in_order(self):
        tree_results = []
        def in_order_visit(node):
            if node.left_child:
                in_order_visit(node.left_child)
            tree_results.append(node.value)
            if node.right_child:
                in_order_visit(node.right_child)
        in_order_visit(self.root)
        return tree_results

    def pre_order(self):
        tree_results = []
        def pre_order_visit(node):
            tree_results.append(node.value)
            if node.left_child:
                pre_order_visit(node.left_child)
            if node.right_child:
                pre_order_visit(node.right_child)
        pre_order_visit(self.root)
        return tree_results

    def post_order(self):
        tree_results = []
        def post_order_visit(node):
            if node.left_child:
                post_order_visit(node.left_child)
            if node.right_child:
                post_order_visit(node.right_child)
            tree_results.append(node.value)
        post_order_visit(self.root)
        return tree_results