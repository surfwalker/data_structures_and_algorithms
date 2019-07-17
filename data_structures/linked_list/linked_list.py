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

    # I obtained some help in creating this method from the following site https://codereview.stackexchange.com/questions/114817/node-link-node-link-node-linking-nodes-into-a-linkedlist
    def ll_kth_from_end(self, k):
        if type(k) is not int:
            return 'Value entered must be an integer.'
        if not self.head:
            return 'This is an empty linked list.'
        linked_list_length = []
        current = self.head
        while current:
            linked_list_length.append(current.value)
            current = current.next
        if k > len(linked_list_length):
            return 'Value entered is larger than the length of the linked list.'
        
        return linked_list_length[len(linked_list_length) - k]

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
