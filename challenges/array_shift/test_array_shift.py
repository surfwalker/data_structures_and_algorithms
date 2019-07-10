from array_shift import insert_shift_array


def test_function_exists():
    assert insert_shift_array

def test_insert_to_middle():
    expected = [1, 2, 3]
    actual = insert_shift_array([1, 3], 2)
    assert expected == actual