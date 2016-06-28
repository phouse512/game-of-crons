import enum


@enum.unique
class Status(enum.Enum):
    EMPTY = 0
    CRON = 1


@enum.unique
class Energy(enum.Enum):
    MAX = 100
    MIN = 0
    SOME = 33