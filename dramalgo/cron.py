

class Cron:

    def __init__(self, x: int, y: int) -> None:
        self.life = 0
        self.x = x
        self.y = y

    """
    set a new position for a cron instance
    """
    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
