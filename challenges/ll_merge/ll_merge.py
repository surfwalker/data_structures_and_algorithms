def ll_merge(self, ll_2):

    if not self.head and not ll_2.head:
        return 'Both linked lists are empty'
    elif self.head and not ll_2.head:
        return self.head
    elif ll_2.head and not self.head:
        return ll_2.head

    if self.head and ll_2.head:
        current_1 = self.head
        current_2 = ll_2.head

        while current_1.next is not None and current_2.next is not None:
            pointer_1 = current_1.next
            pointer_2 = current_2.next

            current_1.next = current_2
            current_2.next = pointer_1

            current_1 = pointer_1
            current_2 = pointer_2

        if current_1.next is None and current_2:
            current_1.next = current_2
            return self.head
            
        if current_2.next is None and current_1:
            pointer_1 = current_1.next
            current_1.next = current_2
            current_2.next = pointer_1
            return self.head
