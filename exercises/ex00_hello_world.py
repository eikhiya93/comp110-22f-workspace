"""My first program for COMP110."""

__author__ = "730597174"

print("Hello, world.")



point_1: list[float] = [3.0, 9.0]
point_2: list[float] = [2.0, 4.0]

from math import sqrt
d: float = sqrt((((point_2[0] - point_1[0])) ** 2) + ((point_2[1] - point_1[1]) ** 2))
print(d)
