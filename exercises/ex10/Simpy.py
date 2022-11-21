"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730597174"


class Simpy:
    """Utility class that is helpful for working with sequences of numerical data."""
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]) -> list[float]:
        """Initialize the values attribute on the object to the argument passed in."""
        self.values = values 

    def __repr__(self) -> str:
        """Convert a Simpy object to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, int_value: int) -> None:
        """Produce a list of the given float value time the given int value."""
        i: int = 0
        self.values = []
        while i < int_value:
            self.values.append(float_value)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Similar to the built-in range function but can take in float number."""
        assert step != 0.0
        self.values = []
        i: float = start
        while i < stop or i > stop:
            self.values.append(i)
            i += step

    def sum(self) -> float:
        """Compute and return the sum of all items in a list."""
        result: float = 0.0
        for _ in self.values:
            result = sum(self.values)
        return result
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Add two lists together at the same index or add each item by a given float value."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        return result

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Given two lists, raise the first item in the first list to the power of the value in the second list or a given float value."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values: 
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        return result 

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return True if items in both lists equal to each other and False otherwise."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        return result 

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return True if the value in the first list is greater than the second list or a given float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        return result 

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allow the ability to use the subscription operaor with Simpy objects."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            ls: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    ls.append(self.values[i])
            return Simpy(ls) 