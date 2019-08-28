from hashtable import HashTable
from linked_list import LinkedList, Node
from repeated_word import repeated_word
import pytest

def test_HashTable_exists():
    assert HashTable

def test_instantiate_HashTable():
    assert HashTable()

def test_LinkedList_exists():
    assert LinkedList

def test_instantiate_LinkedList():
    assert LinkedList()

def test_Node_exists():
    assert Node

def test_instantiate_Node():
    assert Node('value')

def test_repeated_word_one_word_duplicated_no_puntuation():
    str = "This is a sentence that has only one word duplicated in the sentence"
    expected = 'sentence'.upper()
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_many_words_duplicated_no_puntuation():
    str = "This is a sentence that has only many words duplicated in the words sentence and that also has no puntuation but just words"
    expected = 'words'.upper()
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_empty():
    str = ""
    expected = None
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_one_word_duplicated_with_puntuation():
    str = "This is a sentence - that has only one word duplicated in, the sentence and has punctuation."
    expected = 'sentence'.upper()
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_many_words_duplicated_with_puntuation():
    str = "This is a - sentence that has only, many words duplicated in the words sentence and that also has no puntuation but just words."
    expected = 'words'.upper()
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_no_duplicates_no_punctuation():
    str = 'This sentence has no duplicate words and zero punctiation'
    expected = None
    actual = repeated_word(str)
    assert expected == actual

def test_repeated_word_no_duplicates_with_punctuation():
    str = 'This sentence - has no duplicate, words and, some punctiation.'
    expected = None
    actual = repeated_word(str)
    assert expected == actual