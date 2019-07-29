from linked_list import LinkedList

def ll_merge(ll_1, ll_2):

    if not ll_1.head and not ll_2.head:
        return 'Both linked lists are empty'
    elif ll_1.head and not ll_2.head:
        return ll_1.head
    elif ll_2.head and not ll_1.head:
        return ll_2.head

    if ll_1.head and ll_2.head:
        current_1 = ll_1.head
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
            return ll_1.head
            
        if current_2.next is None and current_1:
            pointer_1 = current_1.next
            current_1.next = current_2
            current_2.next = pointer_1
            return ll_1.head
