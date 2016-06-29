"""
contains the World class which contains all of the world data
"""
import random

from dramalgo.cron import Cron
from dramalgo.enums import Energy
from dramalgo.enums import Status
from typing import Any
from typing import Callable


class World:

    """
    basic blind constructor that creates an empty world
    """
    def __init__(self, width: int=10, height: int=10) -> None:
        self.world = [[Space(x, y) for x in range(width)] for y in range(height)]
        self.cells = {} # type: Dict[str, Cron]

        self.age = 0

    def console_output(self, verbose: bool=False) -> None:

        if verbose:
            print("verbose")

        print("\n\n")
        print("--------------------------------\n")
        print("| Day: %s |\n" % self.age)
        print("--------------------------------\n")

        for y in self.world:
            string = "| "
            for x in y:
                string += str(x)
            string += " |"
            print(string)

    """
    iterates over all spaces and applies a supplied method
    """
    def apply_to_spaces(self, func: Callable[Any]) -> None:
        for y in self.world:
            for x in y:
                func(x)

     """
    iterates over all spaces and applies a supplied method
    """


class Space:

    def __init__(self, x: int, y: int, energy: Energy=Energy.MIN) -> None:
        self.x = x
        self.y = y
        self.status = Status.EMPTY
        self.energy = energy

    def __str__(self) -> str:
        return "(%d, %d)" % (self.x, self.y)
