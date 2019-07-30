from tree import BinaryTree

def fizz_buzz_tree(tree):

    def evaluate(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = 'FizzBuzz'
        elif node.value % 3 == 0:
            node.value = 'Fizz'
        elif node.value % 5 == 0:
            node.value = 'Buzz'

        if node.left_child:
            evaluate(node.left_child)
            
        if node.right_child:
            evaluate(node.right_child)

    if tree.root:
        evaluate(tree.root)
    
    return tree