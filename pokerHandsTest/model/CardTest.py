__author__ = 'Cyrus'

import unittest

from pokerHands.model.Card import Card
from pokerHands.model.Suit import Suit
from pokerHands.model.Value import Value


class CardTestCase(unittest.TestCase):
    def test_constructor(self):
        card = Card(Suit.Clubs, Value.Eight)
        self.assertEqual(Suit.Clubs, card.suit)
        self.assertEqual(Value.Eight, card.value)

        card2 = Card(Suit.Spades, Value.Ace)
        self.assertEqual(Suit.Spades, card2.suit)
        self.assertEqual(Value.Ace, card2.value)
    def equals(self):
        card = Card(Suit.Clubs, Value.Eight)
        equal_card = Card(Suit.Clubs, Value.Eight)
        not_equal_different_suit = Card(Suit.Spades, Value.Eight)
        not_equal_different_value = Card(Suit.Clubs, Value.Seven)
        not_equal_different_everything = Card(Suit.Diamonds, Value.Seven)

        self.assertEqual(card, equal_card)
        self.assertNotEquals(card, not_equal_different_suit)
        self.assertNotEquals(card, not_equal_different_value)
        self.assertNotEquals(card, not_equal_different_everything)

