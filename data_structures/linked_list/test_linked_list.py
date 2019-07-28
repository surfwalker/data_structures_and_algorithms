from linked_list import LinkedList
import pytest, sys

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

def test_insert_multiple():
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

def test_append_new_node_to_end_of_linked_list():
    ll = LinkedList()
    ll.insert([2])
    ll.insert([3])
    ll.insert([1])
    ll.append([5])
    assert ll.__str__() == '[1], [3], [2], [5], '

def test_append_new_node_to_empty_linked_list():
    ll = LinkedList()
    ll.append([1])
    assert ll.__str__() == '[1], '

def test_insert_before():
    ll = LinkedList()
    ll.append([1])
    ll.append([3])
    ll.append([2])
    ll.insert_before([3], [5])
    assert ll.__str__() == '[1], [5], [3], [2], '

def test_insert_before_into_empty_linked_list():
    ll = LinkedList()
    ll.insert_before([3], [5])
    assert ll.__str__() == '[5], '

def test_insert_after():
    ll = LinkedList()
    ll.append([1])
    ll.append([3])
    ll.append([2])
    ll.insert_after([3], [5])
    assert ll.__str__() == '[1], [3], [5], [2], '

def test_insert_after_into_empty_linked_list():
    ll = LinkedList()
    ll.insert_before([3], [5])
    assert ll.__str__() == '[5], '

def test_ll_kth_from_end_animals():
    ll = LinkedList()
    ll.append('donkey')
    ll.append('monkey')
    ll.append('camel')
    ll.append('sloth')
    ll.append('shark')
    ll.append('golden unicorn')
    ll.append('kitteh')
    assert ll.ll_kth_from_end(0) == 'kitteh'
    assert ll.ll_kth_from_end(1) == 'golden unicorn'
    assert ll.ll_kth_from_end(2) == 'shark'
    assert ll.ll_kth_from_end(3) == 'sloth'
    assert ll.ll_kth_from_end(4) == 'camel'
    assert ll.ll_kth_from_end(5) == 'monkey'
    assert ll.ll_kth_from_end(6) == 'donkey'

def test_ll_kth_from_end_integers():
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    assert ll.ll_kth_from_end(0) == 2
    assert ll.ll_kth_from_end(1) == 8
    assert ll.ll_kth_from_end(2) == 3
    assert ll.ll_kth_from_end(3) == 1

def test_ll_kth_from_end_one_value():
    ll = LinkedList()
    ll.append(1)
    assert ll.ll_kth_from_end(1) == 1