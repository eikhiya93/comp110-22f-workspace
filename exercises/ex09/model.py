"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt 


__author__ = "730597174"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, point_2: Point) -> float:
        """Compute the distance between two cells."""
        x_component: float = (self.x - point_2.x) ** 2
        y_component: float = (self.y - point_2.y) ** 2
        points_distance: float = sqrt(x_component + y_component)
        return points_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "blue"        

    def contract_disease(self) -> None:
        """Assign the infected constant to the sickness attribute of the cell object the method is call on."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Assign True when a cell is vulnerable and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False 

    def is_infected(self) -> bool:
        """Return True when the cell is infected and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, cell: Cell) -> None:
        """If a vulnerable cell comes in contact with an infected cell, the vulnerable cell becomes infected."""
        if self.is_infected() and cell.is_vulnerable():
            cell.contract_disease()
        if self.is_vulnerable() and cell.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """When assign to a cell, the cell beomes immune to the sickness."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Assign True when cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True 


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, start_sickness: int, start_immune: int = 0):
        """Initialize the cells with random locations and directions and the number of starting cell that is infected."""
        self.population = []
        if start_sickness >= cells:
            raise ValueError("You cannot have starting infected cell be equal to or greater than the population.")
        if start_sickness <= 0:
            raise ValueError("You cannot have starting infected cell be zero or less than the population.")
        if start_immune >= cells:
            raise ValueError("The number of immune cells cannot equal to or be greater than the population.")
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(start_sickness):
            self.population[i].contract_disease()
        for i in range(start_sickness, start_sickness + start_immune):
            self.population[i].immunize()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Check if two cells come in contact."""
        i: int = 0
        while i < len(self.population):
            second_counter: int = i + 1
            while second_counter < len(self.population):
                result_distance = self.population[second_counter].location.distance(self.population[i].location)
                if result_distance < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[second_counter])
                second_counter += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True 