"""Continue practicing with class diagram."""
from __future__ import annotations


class Point:
    """Model a 2D Point."""

    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Initiallize a point with its x, y components."""
        self.x = x
        self.y = y

    def scale_by(self, factor: float) -> None:
        """Mutates: mutiplies components by factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Pure method that does not mutate the Point."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    

p0: Point = Point(1.0, 2.0)
p0.scale_by(2.0)
p1: Point = p0.scale(2.0)
print(f"p0: ({p0.x}, {p0.y}) - p1: ({p1.x}, {p1.y})")
