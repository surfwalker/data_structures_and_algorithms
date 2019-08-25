class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.peek():
          node = self.top
          self.top = self.top.next
          return node.value
        else:
          return None