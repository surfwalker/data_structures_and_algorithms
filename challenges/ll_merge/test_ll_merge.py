from linked_list import LinkedList
from ll_merge import ll_merge

def test_ll_merge_same_length():
    
    animals = LinkedList()
    animals.insert('monkey')
    animals.insert('donkey')
    animals.insert('camel')
    animals.insert('sloth')
    animals.insert('shark')

    waves = LinkedList()
    waves.insert('pipeline')
    waves.insert('mundaka')
    waves.insert('j-bay')
    waves.insert('peahi')
    waves.insert('thurso east')

    expected = animals.head
    actual = ll_merge(animals, waves)
    assert expected == actual


def test_ll_merge_both_empty():
    
    animals = LinkedList()
    waves = LinkedList()

    expected = 'Both linked lists are empty'
    actual = ll_merge(animals, waves)

    assert expected == actual


def test_ll_merge_different_lengths():
    
    animals = LinkedList()
    animals.insert('monkey')
    animals.insert('donkey')
    animals.insert('camel')

    waves = LinkedList()
    waves.insert('pipeline')
    waves.insert('mundaka')

    expected = animals.head
    actual = ll_merge(animals, waves)

    assert expected == actual


def test_ll_merge_one_empty():
    
    animals = LinkedList()
    animals.insert('apples')
    animals.insert('bananas')
    animals.insert('pears')

    waves = LinkedList()

    expected = animals.head
    actual = ll_merge(animals, waves)

    assert expected == actual