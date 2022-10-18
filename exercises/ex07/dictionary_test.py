"""Unit test for the dictionary functions."""

__author__ = "730597174"

from turtle import color
from exercises.ex07.dictionary import invert, favorite_color, count


# Test for invert function


def test_invert_empty() -> None:
    """Test to invert an empty list."""
    a_dict: dict[str, str] = {}
    assert invert(a_dict) == {}


def test_invert_single() -> None:
    """Test to invert a single key-value pair."""
    a_dict: dict[str, str] = {'a': 'x'}
    assert invert(a_dict) == {'x': 'a'}


def test_invert_multi() -> None:
    """Test to invert mulitple key-value pairs."""
    a_dict: dict[str, str] = {'a': 'x', 'b': 'y', 'c': 'z'}
    assert invert(a_dict) == {'x': 'a', 'y': 'b', 'z': 'c'}


# Test for favorite_color function 


def test_one_color() -> None:
    """Test for a list with all color only appear one time."""
    color_dict: dict[str, str] = {'Tun': 'red', 'UNC': 'blue', 'Duke': 'violet', 'NCSU': 'pink'}
    assert favorite_color(color_dict) == 'red'


def test_tie_for_most() -> None:
    """Test for a tie between two colors and return the color that appear first."""
    color_dict: dict[str, str] = {'Tun': 'red', 'UNC': 'blue', 'Duke': 'blue', 'NCSU': 'red'}
    assert favorite_color(color_dict) == 'red'


def test_empty_dict() -> None:
    """Test for empty dictionary and return empty string."""
    color_dict: dict[str, str] = {}
    assert favorite_color(color_dict) == ""


# Test for count function 


def test_empty_list() -> None:
    """Test for an empty list."""
    a_list: list[str] = []
    assert count(a_list) == {}


def test_same_item() -> None:
    """Test for one item but appear multiple time."""
    a_list: list[str] = ['a', 'a', 'a']
    assert count(a_list) == {'a': 3}


def test_diff_item() -> None:
    """Test for multiple items appearing different amount of time."""
    a_list: list[str] = ['a', 'b', 't', 'a', 'p', 'a', 'p', 't']
    assert count(a_list) == {'a': 3, 'b': 1, 't': 2, 'p': 2}
