from dramalgo.cron import Cron
from dramalgo.enums import Energy
from dramalgo.enums import Status
from typing import Callable


class World:

    """
    basic blind constructor that creates an empty world
    """
    def __init__(self, width: int=10, height: int=10) -> None:
        self.world = [[Space(x, y) for x in range(width)] for y in range(height)]
        self.cells = {}  # type: Dict[str, Cron]

        self.age = 0  # type: int

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

    @staticmethod
    def hash_cron(x: int, y: int):
        return "%d_%d_cron" % (x, y)

    """
    iterates over all spaces and applies a supplied method
    """
    def apply_to_spaces(self, apply: Callable[[Space], None]) -> None:
        for y in self.world:
            for x in y:
                apply(x)

    """
    iterates over all crons and applies a supplied method
    """
    def apply_to_crons(self, apply: Callable[[Cron], None]) -> None:
        for cron in self.cells:
            apply(self.cells[cron])

    """
    handle placing a cron at a given space in a world, returns a boolean
      based on whether or not it can
    """
    def place_cron(self, x: int, y: int, cron: Cron) -> bool:
        if self.world[y][x] == Status.CRON:
            return False

        self.world[y][x] = Status.CRON  # bump status at position to taken
        self.cells[World.hash_cron(x, y)] = cron  # add cron to world cron dict
        cron.set_position(x, y)  # update cron's x/y pointer
        

class Space:

    def __init__(self, x: int, y: int, energy: Energy=Energy.MIN) -> None:
        self.x = x
        self.y = y
        self.status = Status.EMPTY
        self.energy = energy

    def __str__(self) -> str:
        return "(%d, %d)" % (self.x, self.y)
