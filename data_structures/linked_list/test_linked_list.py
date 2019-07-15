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

def test_insert_falafel_to_cucumber():
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
    assert ll.__str__() == 'camel, monkey, donkey, '

def test_empty__str__():
    ll = LinkedList()
    assert ll.__str__() == ''