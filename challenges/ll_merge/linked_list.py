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

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.insert(value)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            self.size += 1

    def insert_before(self, value, new_value):
        # need to add exception for if value does not exist
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    self.size += 1
                    break
                else:
                    current = current.next

    def insert_after(self, value, new_value):
        # need to add exception for if value does not exist
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next.next
                    current = current.next
                    current.next = new_node
                    self.size += 1
                    break
                else:
                    current = current.next

    def ll_kth_from_end(self, k):
        if type(k) is not int:
            return 'Value entered must be an integer.'
        if not self.head:
            return 'This is an empty linked list.'
        ll_length = self.size
        current = self.head
        for i in range((ll_length - 1) - k):
            current = current.next
        return current.value