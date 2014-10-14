import unittest
from pokerHands.model.Hand import Hand
from pokerHands.model.Card import Card
from pokerHands.model.Suit import Suit
from pokerHands.model.Value import Value

__author__ = 'Cyrus'


class HandTestCase(unittest.TestCase):
    def test_get_cards_will_sort_by_value(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Eight)
        card3 = Card(Suit.Clubs, Value.Four)
        card4 = Card(Suit.Hearts, Value.Nine)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card3, hand.cards[0])
        self.assertEqual(card5, hand.cards[1])
        self.assertEqual(card2, hand.cards[2])
        self.assertEqual(card4, hand.cards[3])
        self.assertEqual(card1, hand.cards[4])

    def test_get_cards_will_sort_by_value_with_similar_values(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Ace)
        card3 = Card(Suit.Clubs, Value.Four)
        card4 = Card(Suit.Hearts, Value.Nine)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card3, hand.cards[0])
        self.assertEqual(card5, hand.cards[1])
        self.assertEqual(card4, hand.cards[2])
        self.assertEqual(card1, hand.cards[3])
        self.assertEqual(card2, hand.cards[4])

    def test_get_high_card(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Six)
        card3 = Card(Suit.Clubs, Value.Four)
        card4 = Card(Suit.Hearts, Value.Nine)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card1, hand.high_card())

    def test_get_pair_values(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Ace)
        card3 = Card(Suit.Clubs, Value.Four)
        card4 = Card(Suit.Hearts, Value.Nine)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(1, len(hand.get_pairs()))
        self.assertEqual(Value.Ace, hand.get_pairs()[0])

    def test_get_pair_values_when_there_is_more_than_one_pair(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Ace)
        card3 = Card(Suit.Clubs, Value.Four)
        card4 = Card(Suit.Hearts, Value.Four)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(2, len(hand.get_pairs()))
        self.assertEqual(Value.Four, hand.get_pairs()[0])
        self.assertEqual(Value.Ace, hand.get_pairs()[1])

    def test_get_three_of_a_kind_value(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Ten)
        card3 = Card(Suit.Clubs, Value.Ten)
        card4 = Card(Suit.Hearts, Value.Ten)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Value.Ten, hand.get_three_of_a_kind())

    def test_get_three_of_a_kind_value_when_there_are_not_three_of_a_kind(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Ten)
        card3 = Card(Suit.Clubs, Value.Eight)
        card4 = Card(Suit.Hearts, Value.Jack)
        card5 = Card(Suit.Spades, Value.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Value.NULL, hand.get_three_of_a_kind())


    def test_get_four_of_a_kind_value(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Six)
        card3 = Card(Suit.Clubs, Value.Six)
        card4 = Card(Suit.Hearts, Value.Six)
        card5 = Card(Suit.Spades, Value.Six)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Value.Six, hand.get_four_of_a_kind())


    def test_get_four_of_a_kind_value_when_there_are_not_four_of_a_kind(self):
        card1 = Card(Suit.Clubs, Value.Ace)
        card2 = Card(Suit.Diamonds, Value.Six)
        card3 = Card(Suit.Clubs, Value.Five)
        card4 = Card(Suit.Hearts, Value.Queen)
        card5 = Card(Suit.Spades, Value.King)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Value.NULL, hand.get_four_of_a_kind())
