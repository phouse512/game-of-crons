import random


class Cron:
    BASE_ENERGY_COST = 20

    def __init__(self, x: int, y: int, burn_rate: float=0, hit_points: int=5) -> None:
        assert burn_rate <= 2
        assert burn_rate >= -2

        self.life = 0
        self.x = x
        self.y = y
        self.durability = .5  # type: float
        # burn rate is [-2, 2] with step .1
        self.burn_rate = burn_rate  # type: float
        self.hit_points = hit_points

    def set_position(self, x: int, y: int) -> None:
        """
        set a new position for a cron instance
        """
        self.x = x  # type: int
        self.y = y  # type: int

    def get_energy_cost(self):
        """
        calculate the energy cost for a given turn for a cron instance
        """
        return Cron.BASE_ENERGY_COST + round((self.burn_rate + random.randrange(-.4, .4, .2)) * 5)


