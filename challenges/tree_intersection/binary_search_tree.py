from node import Node
from binary_tree import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def add(self, value):
        node = Node(value)
        self.add_node(node)

    def add_node(self, node, current=None):
        if self.root is None:
            self.root = node
        if current is None:
            current = self.root
        if current:
            if current.value > node.value:
                if current.left_child is None:
                    current.left_child = node
                else:
                    self.add_node(node, current.left_child)
            if current.value < node.value:
                if current.right_child is None:
                    current.right_child = node
                else:
                    self.add_node(node, current.right_child)

    def contains(self, value):
        current = self.root
        if self.root is None:
            return False
        while value != current.value:
            if value < current.value and current.left_child:
                current = current.left_child
            elif value > current.value and current.right_child:
                current = current.right_child
            else:
                return False
        return True