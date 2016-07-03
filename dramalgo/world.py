import random

from dramalgo.cron import Cron
from dramalgo.enums import Energy
from dramalgo.enums import Status
from dramalgo.space import Space
from typing import Any
from typing import Callable
from typing import Dict
from typing import Tuple


class World:

    """
    basic blind constructor that creates an empty world
    """
    def __init__(self, width: int=10, height: int=10) -> None:
        self.world = [[Space(x, y) for x in range(width)] for y in range(height)]
        self.cells = {}  # type: Dict[str, Cron]

        self.age = 0  # type: int
        self.width = width  # type: int
        self.height = height  # type: int

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

    def apply_to_spaces(self, apply: Callable[[Space], None]) -> None:
        """
        iterates over all spaces and applies a supplied method
        """
        for y in self.world:
            for x in y:
                apply(x)

    def apply_to_crons(self, apply: Callable[[Cron], None]) -> None:
        """
        iterates over all crons and applies a supplied method
        """
        for cron in self.cells:
            apply(self.cells[cron])

    def place_cron(self, x: int, y: int, cron: Cron) -> bool:
        """
        handle placing a cron at a given space in a world, returns a boolean
          based on whether or not it can
        """
        if self.world[y][x] == Status.CRON:
            return False

        self.world[y][x].status = Status.CRON  # bump status at position to taken
        self.cells[World.hash_cron(x, y)] = cron  # add cron to world cron dict
        cron.set_position(x, y)  # update cron's x/y pointer

    def seed_world(self, seed: str='', full: float=.05) -> None:
        """
        clears the world and randomly places new crons and food stashes all over the map
        :param seed: an optional param that overrides the default python seeding
        :param full: how many spots seed should proportionally fill
        """
        if seed:
            random.seed(seed)

        open_spaces = []  # type: List[Tuple[int, int]]

        # TODO: change this to be simple list comprehension using self.height/width
        for y in self.world:
            for x in y:
                open_spaces.append((x.x, x.y))

        # TODO: change this to have some variation
        random_spots = int(full * self.height * self.width)  # type: int
        for i in range(random_spots):
            position = random.randint(0, len(open_spaces)-1)
            x_ind, y_ind = open_spaces[position][0], open_spaces[position][1]
            self.place_cron(x_ind, y_ind, Cron(x_ind, y_ind))
            open_spaces.pop(position)

        self.seed_food()

    def seed_food(self) -> None:
        """
        populates the map with random placements of food, right now it is even, but ideally
          there will be *smart* grouping in the future
        :return:
        """

        open_spaces = []  # type: List[Tuple[int, int]]

        # TODO: change this to be simple list comprehension using self.height/width
        for y in self.world:
            for x in y:
                open_spaces.append((x.x, x.y))

        food_range = random.choice([x * .01 for x in range(5, 15)])  # type: float
        random_food = int(food_range * self.width * self.height)  # type: int

        # iterate over random food, the number of food spots to place and randomly select
        #   an open position for each piece of energy
        for i in range(random_food):
            position = random.randint(0, len(open_spaces)-1)  # type: int
            x_ind, y_ind = open_spaces[position][0], open_spaces[position][1]
            self.world[y_ind][x_ind].energy = Energy.select_random()
            open_spaces.pop(position)

    def tick(self) -> Dict[Any, Any]:
        """
        advance the world by 1 day - call the necessary code on each cron, replenish
          energy stores, etc
        :return: a dict of the diff between map renders
        """
        self.consume_food()

        # TODO: foreach cron, fetch food from that space

    def consume_food(self) -> None:
        """
        attempt to feed all circles based on whatever spaces they inhabit - loop
          through self.cells
        """

        for key, value in self.cells.items():
            space = self.world[value.y][value.x]
            print(space.energy)

    def reset_world(self) -> None:
        """
        destroys and clears world to be empty
        :param persist: an optional boolean that allows for the world to be saved to disk before clearing
        """
        self.world = [[Space(x, y) for x in range(self.width)] for y in range(self.height)]
        self.cells = {}
        self.age = 0
