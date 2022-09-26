"""Practicing with list and utility functions."""

__author__ = "730597174"

# Part 1: Defining and creating lists functions. 


def all(a: list[int], b: list[int]) -> bool: 
    """A function for matching if an integer matches all the list."""
    i: int = 0 
    list_match: bool = False
    while i < len(a): 
        if a[i] == b:
            list_match = True 
            i += 1
        else: 
            return False 
    return list_match


# Part 2: Define max


def max(c: list[int]) -> int: 
    """Return the largest number in the list."""
    largest: int = 0
    i: int = 0
    if len(c) == 0:
        raise ValueError ("max() arg is an empy List")
    while i < len(c):
        if c[i] > c[len(c) - 1]:
            largest = c[i]
            i += 1
        else:
            i += 1
    return largest


# Part 3: Define is_equal 


def is_equal(e: list[int], f: list[int]) -> bool: 
    """Check to see if every items on both lists are equal."""
    i: int = 0
    match: bool = False
    while i < len(e or f): 
        if e[i] == f[i] and len(e) == len(f):
            match = True 
            i += 1
        else: 
            return False 
    return match
