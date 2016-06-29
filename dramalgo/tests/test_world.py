import unittest

from dramalgo.world import World


class TestWorld(unittest.TestCase):

    def test_hash_cron(self):
        result = World.hash_cron(10, 10)
        self.assertEqual("10_10_cron", result)
