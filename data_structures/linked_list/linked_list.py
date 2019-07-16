class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        returned_str = ''
        current = self.head
        while current:
            returned_str += f'{current.value}'
            current = current.next
        return returned_str

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
    
    def insert_before(self, value, new_value):
        # need to add exception for if value does not exist
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == value:
                    new_node.next = current.next
                    current.next = new_node
                    break
                else:
                    current = current.next

    def insert_after(self, value, new_value):
        # need to add exception for if value does not exist 
        new_node = Node(new_value)

        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    new_node.next = current.next.next
                    current = current.next
                    current.next = new_node
                    break
                else:
                    current = current.next

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next