import unittest
from dramalgo.cron import Cron
from unittest.mock import patch


class TestCron(unittest.TestCase):

    @patch('dramalgo.cron.random.randrange')
    def test_get_energy_cost(self, mock_rand):
        cron = Cron(0, 0, burn_rate=.5)
        mock_rand.return_value = -.4

        result = cron.get_energy_cost()
        self.assertEqual(20, result)
        mock_rand.assert_called_with(-.4, .4, .2)

    @patch('dramalgo.cron.random.randrange')
    def test_get_energy_cost_2(self, mock_rand):
        cron = Cron(0, 0, burn_rate=2)
        mock_rand.return_value = .4

        result = cron.get_energy_cost()
        self.assertEqual(32, result)
        mock_rand.assert_called_with(-.4, .4, .2)

    def test_cron_burn_rate_limit(self):
        self.assertRaises(AssertionError, Cron, 0, 0, -2.1)
        self.assertRaises(AssertionError, Cron, 0, 0, 2.1)
        self.assertEqual(2, Cron(0, 0, burn_rate=2).burn_rate)
        self.assertEqual(-2, Cron(0, 0, burn_rate=-2).burn_rate)
