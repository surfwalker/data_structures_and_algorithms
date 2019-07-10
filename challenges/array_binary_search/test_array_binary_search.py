from array_binary_search import array_binary_search

def test_function_exists():
    assert array_binary_search

def test_returns_index_for_even_length_lst():
    expected = 2
    actual = array_binary_search([4,8,15,16,23,42], 15)
    assert expected == actual

def test_returns_index_for_odd_length_lst():
    expected = 2
    actual = array_binary_search([4,8,15,16,23,42,55], 15)
    assert expected == actual

def test_returns_negative_one_if_value_does_not_exist():
    expected = -1
    actual = array_binary_search([11,22,33,44,55,66,77], 90)
    assert expected == actual

def test_empty_lst():
    expected = -1
    actual = array_binary_search([], 20)
    assert expected == actual