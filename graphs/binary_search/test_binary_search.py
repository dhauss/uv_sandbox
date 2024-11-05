import pytest

from binary_search import binary_search_iterative, binary_search_recursive

@pytest.fixture
def arr_odd():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def arr_even():
    return [1, 2, 3, 4]

@pytest.fixture
def arr_single():
    return [1]

@pytest.fixture
def arr_empty():
    return []

def test_binary_search_it(arr_odd, arr_even, arr_single, arr_empty):
    assert binary_search_iterative(arr_odd, 0) == -1
    assert binary_search_iterative(arr_odd, 1) == 0
    assert binary_search_iterative(arr_odd, 2) == 1
    assert binary_search_iterative(arr_odd, 3) == 2
    assert binary_search_iterative(arr_odd, 4) == 3
    assert binary_search_iterative(arr_odd, 5) == 4

    assert binary_search_iterative(arr_even, 1) == 0
    assert binary_search_iterative(arr_even, 2) == 1
    assert binary_search_iterative(arr_even, 3) == 2
    assert binary_search_iterative(arr_even, 4) == 3

    assert binary_search_iterative(arr_single, 1) == 0
    
    assert binary_search_iterative(arr_empty, 1) == -1

def test_binary_search_rec(arr_odd, arr_even, arr_single, arr_empty):
    assert binary_search_recursive(arr_odd, 0, 0, len(arr_odd) - 1) == -1
    assert binary_search_recursive(arr_odd, 1, 0, len(arr_odd) - 1) == 0
    assert binary_search_recursive(arr_odd, 2, 0, len(arr_odd) - 1) == 1
    assert binary_search_recursive(arr_odd, 3, 0, len(arr_odd) - 1) == 2
    assert binary_search_recursive(arr_odd, 4, 0, len(arr_odd) - 1) == 3
    assert binary_search_recursive(arr_odd, 5, 0, len(arr_odd) - 1) == 4

    assert binary_search_recursive(arr_even, 1, 0, len(arr_even) - 1) == 0
    assert binary_search_recursive(arr_even, 2, 0, len(arr_even) - 1) == 1
    assert binary_search_recursive(arr_even, 3, 0, len(arr_even) - 1) == 2
    assert binary_search_recursive(arr_even, 4, 0, len(arr_even) - 1) == 3

    assert binary_search_recursive(arr_single, 1, 0, len(arr_single) - 1) == 0
    
    assert binary_search_recursive(arr_empty, 1, 0, len(arr_empty) - 1) == -1