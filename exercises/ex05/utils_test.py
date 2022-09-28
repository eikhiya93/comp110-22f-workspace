"""Tests for only_evens, concat, and sub function."""

__author__ = "730597174"

# Test for only evens function. 


from exercises.ex05.utils import only_evens

def test_evens_empty() -> None:
    evens_list: list[int] = []
    assert only_evens(evens_list) == []

def test_evens_negative() -> None: 
    evens_list: list[int] = [-2, -1, 0, 1, 2]
    assert only_evens(evens_list) == [-2, 0, 2]

def test_evens_multi() -> None:
    evens_list: list[int] = [5, 6, 7, 8]
    assert only_evens(evens_list) == [6, 8]

# Test for concat function. 

from exercises.ex05.utils import concat

def test_equal_len() -> None:
    a_list: list[int] = [1, 10, 100]
    b_list: list[int] = [200, 20, 2]
    assert concat(a_list, b_list) == [1, 10, 100, 200, 20, 2]

def test_diff_len() -> None:
    a_list: list[int] = [1, 11, 23, 9, -256]
    b_list: list[int] = [45, 57]
    assert concat(a_list, b_list) == [1, 11, 23, 9, -256, 45, 57]

def test_empty_list() -> None: 
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []

# Test for sub function. 


from exercises.ex05.utils import sub

def test_rand_list() -> None:
    a_list: list[int] = [1, 3, 6, 7, 9, 23]
    assert sub(a_list, 2, 10) == [6, 7, 9, 23]

def test_neg_start() -> None:
    a_list: list[int] = [-12, -24, 35, 46, 58, 69]
    assert sub(a_list, -2, 4) == [-12, -24, 35, 46]

def test_empty_list() -> None:
    a_list: list[int] = []
    assert sub(a_list, 2, 4) == []
