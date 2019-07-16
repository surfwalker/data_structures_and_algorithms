from linked_list import LinkedList

def test_exists():
    assert LinkedList

def test_creation():
    ll = LinkedList()
    assert ll

def test_head_is_none():
    ll = LinkedList()
    assert ll.head is None

def test_add_to_empty():
    ll = LinkedList()
    ll.insert('donkey')
    assert ll.head.value == 'donkey'

def test_add_again_to_empty():
    ll = LinkedList()
    ll.insert('monkey')
    assert ll.head.value == 'monkey'

def test_add_to_empty_check_next():
    ll = LinkedList()
    ll.insert('camel')
    assert ll.head.next is None

def test_insert_donkey_to_monkey_to_cucumber():
    ll = LinkedList()
    ll.insert('donkey')
    ll.insert('monkey')
    ll.insert('camel')
    assert ll.head.value == 'camel'
    assert ll.head.next.value == 'monkey'
    assert ll.head.next.next.value == 'donkey'
    assert ll.head.next.next.next is None

def test_includes_empty():
    ll = LinkedList()
    assert not ll.includes('tortoise')

def test_includes():
    ll = LinkedList()
    ll.insert('donkey')
    ll.insert('monkey')
    ll.insert('camel')
    assert ll.includes('donkey')

def test_does_not_includes():
    ll = LinkedList()
    ll.insert('donkey')
    ll.insert('monkey')
    ll.insert('camel')
    assert not ll.includes('sloth')

def test__str__():
    ll = LinkedList()
    ll.insert('donkey')
    ll.insert('monkey')
    ll.insert('camel')
    assert ll.__str__() == 'camelmonkeydonkey'

def test_empty__str__():
    ll = LinkedList()
    assert ll.__str__() == ''

def test_append_new_node_to_end_of_linked_list():
    ll = LinkedList()
    ll.insert([2])
    ll.insert([3])
    ll.insert([1])
    ll.append([5])
    assert ll.__str__() == '[1][3][2][5]'

def test_append_new_node_to_empty_linked_list():
    ll = LinkedList()
    ll.append([1])
    assert ll.__str__() == '[1]'

def test_insert_before():
    ll = LinkedList()
    ll.append([1])
    ll.append([3])
    ll.append([2])
    ll.insert_before([3], [5])
    assert ll.__str__() == '[1][5][3][2]'

def test_insert_before_into_empty_linked_list():
    ll = LinkedList()
    ll.insert_before([3], [5])
    assert ll.__str__() == '[5]'

def test_insert_after():
    ll = LinkedList()
    ll.append([1])
    ll.append([3])
    ll.append([2])
    ll.insert_after([3], [5])
    assert ll.__str__() == '[1][3][5][2]'

def test_insert_after_into_empty_linked_list():
    ll = LinkedList()
    ll.insert_before([3], [5])
    assert ll.__str__() == '[5]'