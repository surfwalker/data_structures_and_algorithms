import pytest
from quick_sort import quick_sort

def test_quick_sort_exists():
    assert quick_sort

def test_quick_sort_one():
    lst = [7]
    expected = "List is already sorted."
    actual = quick_sort(lst, 0, len(lst) - 1)
    assert actual == expected

def test_sorted_list_even_numbers():
    lst = [2, 4, 8, 10, 12, 22, 32]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [2, 4, 8, 10, 12, 22, 32]
    actual = lst
    assert actual == expected

def test_sorted_list_odd_numbers():
    lst = [1, 5, 7, 13, 17, 23, 35]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [1, 5, 7, 13, 17, 23, 35]
    actual = lst
    assert actual == expected

def test_sorted_list_all_numbers():
    lst = [1, 2, 3, 4, 5, 6, 7]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [1, 2, 3, 4, 5, 6, 7]
    actual = lst
    assert actual == expected

def test_unsorted_list_even_numbers():
    lst = [4, 2, 8, 6, 12, 26, 22]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [2, 4, 6, 8, 12, 22, 26]
    actual = lst
    assert actual == expected

def test_unsorted_list_odd_numbers():
    lst = [7, 5, 1, 3, 9, 17, 13]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [1, 3, 5, 7, 9, 13, 17]
    actual = lst
    assert actual == expected

def test_unsorted_list_all_numbers():
    lst = [22, 13, 64, 12, 4, 7, 3]
    quick_sort(lst, 0, len(lst) - 1)
    expected = [3, 4, 7, 12, 13, 22, 64]
    actual = lst
    assert actual == expected

def test_empty_list():
    lst = []
    expected = "This is an empty list."
    actual = quick_sort(lst, 0, len(lst) - 1)
    assert actual == expected