from hashtable import HashTable
import pytest

def test_HashTable_exists():
    assert HashTable

def test_instantiate_HashTable():
    assert HashTable()

def test_hashtable_add():
    ht = HashTable()
    ht.add('pipeline', 'mundaka')
    assert ht.get('pipeline') == 'mundaka'

def test_hashtable_contains_empty():
    ht = HashTable()
    assert not ht.contains('pipeline')

def test_hashtable_contains_one():
    ht = HashTable()
    ht.add('pipeline', 'mundaka')
    assert ht.contains('pipeline')

def test_hashtable_is_same():
    ht = HashTable()
    assert ht.hash('pipeline') == ht.hash('pipeline')

def test_hashtable_is_different():
    ht = HashTable()
    assert not ht.hash('pipeline') == ht.hash('mundaka')

def test_hashtable_collision():
    ht = HashTable()
    ht.add('pipeline', 'mundaka')
    ht.add('log cabins', 'thurso')
    assert ht.get('pipeline') == ('mundaka')
    assert ht.get('log cabins') == ('thurso')

