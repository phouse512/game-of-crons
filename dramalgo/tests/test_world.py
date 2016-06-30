import unittest

from dramalgo.cron import Cron
from dramalgo.enums import Status
from dramalgo.world import World


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.world = World()

    def tearDown(self):
        del self.world

    def test_hash_cron(self):
        result = World.hash_cron(10, 10)
        self.assertEqual("10_10_cron", result)

    def test_place_cron(self):
        test_cron = Cron(1, 1)

        self.world.place_cron(4, 8, test_cron)

        self.assertEqual(4, test_cron.x)
        self.assertEqual(8, test_cron.y)
        self.assertEqual(test_cron, self.world.cells[World.hash_cron(4, 8)])
        self.world.console_output()
        self.assertEqual(Status.CRON, self.world.world[8][4].status)

    def test_reset_world(self):
        test_cron = Cron(1, 1)

        self.world.place_cron(4, 8, test_cron)
        self.world.age = 1
        self.world.reset_world()

        self.assertEqual({}, self.world.cells)
        self.assertEqual(0, self.world.age)
