import time

from dramalgo.world import World


class Dramalgo:

    def __init__(self) -> None:
        print("starting now")

        self.world = World()
        self.run()

    def run(self) -> None:
        print("actually running")
        while True:
            time.sleep(.5)
            print("sleping yo")


def main() -> None:
    Dramalgo()

