__author__ = 'Cyrus'
import unittest
from pokerHands.game.Winner import Winner


class WinnerTestCase(unittest.TestCase):
    def test_enum_value(self):
        self.assertEqual(0, Winner.Tie.value)
        self.assertEqual(1, Winner.Player_One.value)
        self.assertEqual(2, Winner.Player_Two.value)

if __name__ == '__main__':
    unittest.main()