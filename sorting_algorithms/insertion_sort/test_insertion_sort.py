from insertion_sort import insert_sort
import pytest

def test_sorted_list_even_numbers():
    lst = [2, 4, 8, 10, 12, 22, 32]
    expected = [2, 4, 8, 10, 12, 22, 32]
    actual = insert_sort(lst)
    assert actual == expected

def test_sorted_list_odd_numbers():
    lst = [1, 5, 7, 13, 17, 23, 35]
    expected = [1, 5, 7, 13, 17, 23, 35]
    actual = insert_sort(lst)
    assert actual == expected

def test_sorted_list_all_numbers():
    lst = [1, 2, 3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    actual = insert_sort(lst)
    assert actual == expected

def test_unsorted_list_even_numbers():
    lst = [4, 2, 8, 6, 12, 26, 22]
    expected = [2, 4, 6, 8, 12, 22, 26]
    actual = insert_sort(lst)
    assert actual == expected

def test_unsorted_list_odd_numbers():
    lst = [7, 5, 1, 3, 9, 17, 13]
    expected = [1, 3, 5, 7, 9, 13, 17]
    actual = insert_sort(lst)
    assert actual == expected

def test_unsorted_list_all_numbers():
    lst = [22, 13, 64, 12, 4, 7, 3]
    expected = [3, 4, 7, 12, 13, 22, 64]
    actual = insert_sort(lst)
    assert actual == expected

def test_empty_list():
    lst = []
    expected = "This is an empty list."
    actual = insert_sort(lst)
    assert actual == expected