"""
contains the World class which contains all of the world data
"""
from dramalgo.enums import Energy
from dramalgo.enums import Status


class World:

    """
    basic blind constructor that creates an empty world
    """
    def __init__(self, width: int=20, height: int=20) -> None:
        self.world = [[0 for x in range(width)] for y in range(height)]
        print(self.world)

        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                self.world[y][x] = "yes" # "y:%s x: %s" % (str(y), str(x))

        print(self.world)


class Space:

    def __init__(self, x: int, y: int, energy: Energy=Energy.MIN) -> None:
        self.x = x
        self.y = y
        self.status = Status.EMPTY
        self.energy = energy

