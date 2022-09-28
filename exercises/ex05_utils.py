"""Continue practicing with list and utility functions."""

__author__ = "730597174"

# Part 1: Define only_evens function


def only_evens(a: list[int]) -> int: 
    """Defining a function that only return an even numbers in a list."""
    i: int = 0
    track_even: list[int] = list()
    while i < len(a): 
        if a[i] % 2 == 0:
            track_even.append(a[i])
        i += 1
    return track_even

# Part 2: Define concat function


def concat(b: list[int], c: list[int]) -> int: 
    """A function that add two lists. """
    i: int = 0
    tracker: list[int] = list()
    while i < len(b): 
        tracker.append(b[i])
        i += 1
    i_2: int = 0
    while i_2 < len(c): 
        tracker.append(c[i_2]) 
        i_2 += 1 
    return tracker 

# Part 3: Define sub function 


def sub(x: list[int], y: int, z: int) -> list[int]: 
    """A function to generate a second list from a given list within a parameter."""
    sub_list: list[int] = list()
    empty_list: list[int] = list()
    if y < 0:
        y = 0
    if z > len(x): 
        z = len(x) 
    if len(x) == 0:
        return empty_list
    if y > len(x): 
        return empty_list
    if z <= 0:
        return empty_list
    while y <= z - 1: 
        sub_list.append(x[y])
        y += 1
    return sub_list
