from node import Node

class LinkedList:

    def __init__(self, iterable=[]):
        """
        Initialize Linked List.
        """
        self.head = None
        self.size = 0
        if iterable:
            for value in iterable:
                self.insert(value)

    def insert(self, val):
        """
        Insert an item into Linked List.
        """
        self.head = Node(val, self.head)
        self.size += 1

    def includes(self, value):
        """
        Check if Linked List includes a specific value.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        """
        Return all values of each Node in Linked List as a string.
        """
        returned_str = ''
        current = self.head
        while current:
            returned_str += f'{current.value}, '
            current = current.next
        return returned_str