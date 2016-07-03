from dramalgo.enums import Energy
from dramalgo.enums import Status


class Space:

    def __init__(self, x: int, y: int, energy: int=0) -> None:
        self.x = x
        self.y = y
        self.status = Status.EMPTY
        self.energy = energy

    def __str__(self) -> str:
        return "(%d, %d: %s)" % (self.x, self.y, self.status)
