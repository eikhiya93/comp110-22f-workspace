"""Dictionary Functions."""

__author__ = "730597174"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Switch the keys of a dictionary with the values and vice versa."""
    dictionary: dict[str, str] = {}
    for key in a:
        value: str = a[key] 
        if value in dictionary > 1:
            raise KeyError ("Key cannot repeat")
        dictionary[value] = key    
    return dictionary 


def favorite_color(a: dict[str, str]) -> str: 
    """Return the color that appears the most in a dictionary."""
    dictionary: dict[str, int] = {}
    most_frq_color: str = ""
    i: int = 0
    for key in a:
        color = a[key]
        if color in dictionary:
            dictionary[color] += 1
        else:
            dictionary[color] = 1
    for color in dictionary:
        if dictionary[color] > i:
            i = dictionary[color]
            most_frq_color = color 
    return most_frq_color 


def count(a: list[str]) -> dict[str, int]:
    """Count the number of time a word appear in a list."""
    frequency: dict[str, int] = {}
    for key in a:
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1
    return frequency 