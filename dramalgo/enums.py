import enum
import random


@enum.unique
class Status(enum.Enum):
    EMPTY = 0
    CRON = 1


@enum.unique
class Energy(enum.Enum):
    MAX = 100
    NONE = 0
    SOME = 33
    MED = 50
    LARGE = 70

    @staticmethod
    def select_random():
        energy_list = [x for x in Energy]
        return random.choice(energy_list).value
