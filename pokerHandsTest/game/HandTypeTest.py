__author__ = 'Cyrus'

import unittest
from pokerHands.game.HandType import HandType


class HandTypeTestCase(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(1, HandType.High_Card.value)
        self.assertEqual(2, HandType.Two_of_a_Kind.value)
        self.assertEqual(3, HandType.Two_Pair.value)
        self.assertEqual(4, HandType.Three_of_a_Kind.value)
        self.assertEqual(5, HandType.Straight.value)
        self.assertEqual(6, HandType.Flush.value)
        self.assertEqual(7, HandType.Full_House.value)
        self.assertEqual(8, HandType.Four_of_a_Kind.value)
        self.assertEqual(9, HandType.Straight_Flush.value)


if __name__ == '__main__':
    unittest.main()


