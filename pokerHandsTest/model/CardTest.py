__author__ = 'Cyrus'

import unittest

from pokerHands.model.Card import Card
from pokerHands.model.Suit import Suit
from pokerHands.model.Rank import Rank


class CardTestCase(unittest.TestCase):
    def test_constructor(self):
        card = Card(Suit.Clubs, Rank.Eight)
        self.assertEqual(Suit.Clubs, card.suit)
        self.assertEqual(Rank.Eight, card.rank)

        card2 = Card(Suit.Spades, Rank.Ace)
        self.assertEqual(Suit.Spades, card2.suit)
        self.assertEqual(Rank.Ace, card2.rank)
    def equals(self):
        card = Card(Suit.Clubs, Rank.Eight)
        equal_card = Card(Suit.Clubs, Rank.Eight)
        not_equal_different_suit = Card(Suit.Spades, Rank.Eight)
        not_equal_different_value = Card(Suit.Clubs, Rank.Seven)
        not_equal_different_everything = Card(Suit.Diamonds, Rank.Seven)

        self.assertEqual(card, equal_card)
        self.assertNotEquals(card, not_equal_different_suit)
        self.assertNotEquals(card, not_equal_different_value)
        self.assertNotEquals(card, not_equal_different_everything)

if __name__ == '__main__':
    unittest.main()