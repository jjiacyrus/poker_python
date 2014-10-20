from pokerHands.euler.EulerResults import EulerResults

__author__ = 'Cyrus'

import unittest


class EulerResultTestCase(unittest.TestCase):
    def test_properties(self):
        player_one_wins = 125
        player_two_wins = 251
        ties = 123
        results = EulerResults(player_one_wins, player_two_wins, ties)
        self.assertEqual(player_one_wins, results.player_one_wins)
        self.assertEqual(player_two_wins, results.player_two_wins)
        self.assertEqual(ties, results.ties)


if __name__ == '__main__':
    unittest.main()
