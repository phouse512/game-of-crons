from dramalgo.world import World


class Dramalgo:

    def __init__(self) -> None:
        print("starting now")

        self.world = World()
        self.world.seed_world()
        self.run()

    def run(self) -> None:
        print("actually running")


def main() -> None:
    Dramalgo()

