__author__ = 'Cyrus'

import unittest
from pokerHands.model.Rank import Rank


class RankTestCase(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(Rank.NULL.value, 0)
        self.assertEqual(Rank.Two.value, 2)
        self.assertEqual(Rank.Three.value, 3)
        self.assertEqual(Rank.Four.value, 4)
        self.assertEqual(Rank.Five.value, 5)
        self.assertEqual(Rank.Six.value, 6)
        self.assertEqual(Rank.Seven.value, 7)
        self.assertEqual(Rank.Eight.value, 8)
        self.assertEqual(Rank.Nine.value, 9)
        self.assertEqual(Rank.Ten.value, 10)
        self.assertEqual(Rank.Jack.value, 11)
        self.assertEqual(Rank.Queen.value, 12)
        self.assertEqual(Rank.King.value, 13)
        self.assertEqual(Rank.Ace.value, 14)

    def test_is_comparable_less_than(self):
        self.assertTrue(Rank.NULL < Rank.Two)
        self.assertTrue(Rank.Two < Rank.Three)
        self.assertTrue(Rank.Four < Rank.Five)

    def test_is_comparable_greater_than(self):
        self.assertTrue(Rank.Five > Rank.Two)
        self.assertTrue(Rank.Ace > Rank.Three)
        self.assertTrue(Rank.Six > Rank.Five)


    def test_find_by_abbreviation(self):
        self.assertEqual(Rank.Two, Rank.find('2'))
        self.assertEqual(Rank.Three, Rank.find('3'))
        self.assertEqual(Rank.Four, Rank.find('4'))
        self.assertEqual(Rank.Five, Rank.find('5'))
        self.assertEqual(Rank.Six, Rank.find('6'))
        self.assertEqual(Rank.Seven, Rank.find('7'))
        self.assertEqual(Rank.Eight, Rank.find('8'))
        self.assertEqual(Rank.Nine, Rank.find('9'))
        self.assertEqual(Rank.Ten, Rank.find('10'))
        self.assertEqual(Rank.Jack, Rank.find('J'))
        self.assertEqual(Rank.Queen, Rank.find('Q'))
        self.assertEqual(Rank.King, Rank.find('K'))
        self.assertEqual(Rank.Ace, Rank.find('A'))
        self.assertEqual(Rank.NULL, Rank.find('D'))


if __name__ == '__main__':
    unittest.main()