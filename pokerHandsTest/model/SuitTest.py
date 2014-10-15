__author__ = 'Cyrus'

import unittest
from pokerHands.model.Suit import Suit


class SuitTestCase(unittest.TestCase):
    def test_enums(self):
        self.assertEqual(Suit.Clubs, Suit.Clubs)
        self.assertEqual(Suit.Spades, Suit.Spades)
        self.assertEqual(Suit.Hearts, Suit.Hearts)
        self.assertEqual(Suit.Diamonds, Suit.Diamonds)

    def test_find(self):
        self.assertEqual(Suit.Spades, Suit.find('S'))
        self.assertEqual(Suit.Hearts, Suit.find('H'))
        self.assertEqual(Suit.Clubs, Suit.find('C'))
        self.assertEqual(Suit.Diamonds, Suit.find('D'))
        self.assertEqual(Suit.NULL, Suit.find('Z'))

if __name__ == '__main__':
    unittest.main()