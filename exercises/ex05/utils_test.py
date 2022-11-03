"""Tests for only evens, concat, and sub function."""

__author__ = "730597174"

# Test for only evens function. 

from exercises.ex05.utils import only_evens, concat, sub


def test_evens_empty() -> None:
    """Test for empty list."""
    evens_list: list[int] = []
    assert only_evens(evens_list) == []


def test_evens_negative() -> None:
    """Testing for negative number."""
    evens_list: list[int] = [-2, -1, 0, 1, 2]
    assert only_evens(evens_list) == [-2, 0, 2]


def test_evens_multi() -> None:
    """Testing for a multi-random list."""
    evens_list: list[int] = [5, 6, 7, 8]
    assert only_evens(evens_list) == [6, 8]

# Test for concat function. 


def test_equal_len() -> None:
    """Testing for two lists with equal length."""
    a_list: list[int] = [1, 10, 100]
    b_list: list[int] = [200, 20, 2]
    assert concat(a_list, b_list) == [1, 10, 100, 200, 20, 2]


def test_diff_len() -> None:
    """Testing for two lits with different length."""
    a_list: list[int] = [1, 11, 23, 9, -256]
    b_list: list[int] = [45, 57]
    assert concat(a_list, b_list) == [1, 11, 23, 9, -256, 45, 57]


def test_single_list() -> None: 
    """Testing for two lists with one integer."""
    a_list: list[int] = [2]
    b_list: list[int] = [3]
    assert concat(a_list, b_list) == [2, 3]


# Test for sub function. 

def test_rand_list() -> None:
    """Testing for a random list."""
    a_list: list[int] = [1, 3, 6, 7, 9, 23]
    assert sub(a_list, 2, 10) == [6, 7, 9, 23]


def test_neg_start() -> None:
    """Testing for a sub list that start with a negative index."""
    a_list: list[int] = [-12, -24, 35, 46, 58, 69]
    assert sub(a_list, -2, 4) == [-12, -24, 35, 46]


def test_empty_list() -> None:
    """Testing for an empty list."""
    a_list: list[int] = []
    assert sub(a_list, 2, 4) == []
