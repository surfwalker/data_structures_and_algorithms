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

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def insert(self, value):
#         self.head = Node(value, self.head)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# class Stack:

#     def __init__(self):
#         self.lst = LinkedList()
#         self.top = None

#     def peek(self):
#         if self.top:
#             return self.top.value
#         else:
#             return None

#     def pop(self):
#         pass

#     def push(self, value):
#         self.top = Node(value, self.top)