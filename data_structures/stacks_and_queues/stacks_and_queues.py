class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        self.head = Node(val, self.head)

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack:

    def __init__(self):
        self.lst = LinkedList()
        self.top = None

    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None

    def pop(self):
        pass

    def push(self, value):
        self.top = Node(val, self.top)
        


class Quezee():
    # peek
    # enqueue
    # dequeue

    def __init__(self):
        self.lst = LinkedList()

    def peek(self):
        return self.lst.head and self.lst.head.val

    def enqueue(self, value):
        self.lst.insert(value)
    
    def dequeue(self):
        pass
