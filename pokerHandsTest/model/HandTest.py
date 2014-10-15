import unittest
from pokerHands.model.Hand import Hand
from pokerHands.model.Card import Card
from pokerHands.model.Suit import Suit
from pokerHands.model.Rank import Rank

__author__ = 'Cyrus'


class HandTestCase(unittest.TestCase):
    def test_get_cards_will_sort_by_value(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card3, hand.cards[0])
        self.assertEqual(card5, hand.cards[1])
        self.assertEqual(card2, hand.cards[2])
        self.assertEqual(card4, hand.cards[3])
        self.assertEqual(card1, hand.cards[4])

    def test_get_cards_will_sort_by_value_with_similar_values(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Ace)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card3, hand.cards[0])
        self.assertEqual(card5, hand.cards[1])
        self.assertEqual(card4, hand.cards[2])
        self.assertEqual(card1, hand.cards[3])
        self.assertEqual(card2, hand.cards[4])

    def test_get_high_card(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(card1, hand.high_card())

    def test_get_pair_values(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Ace)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(1, len(hand.get_pairs()))
        self.assertEqual(Rank.Ace, hand.get_pairs()[0])

    def test_get_pair_values_when_there_are_none(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Seven)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(0, len(hand.get_pairs()))


    def test_get_pair_values_when_there_is_more_than_one_pair(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Ace)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Four)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(2, len(hand.get_pairs()))
        self.assertEqual(Rank.Four, hand.get_pairs()[0])
        self.assertEqual(Rank.Ace, hand.get_pairs()[1])

    def test_get_three_of_a_kind_value(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Ten)
        card3 = Card(Suit.Clubs, Rank.Ten)
        card4 = Card(Suit.Hearts, Rank.Ten)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.Ten, hand.get_three_of_a_kind())

    def test_get_three_of_a_kind_value_when_there_are_not_three_of_a_kind(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Ten)
        card3 = Card(Suit.Clubs, Rank.Eight)
        card4 = Card(Suit.Hearts, Rank.Jack)
        card5 = Card(Suit.Spades, Rank.Five)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.NULL, hand.get_three_of_a_kind())


    def test_get_four_of_a_kind_value(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Clubs, Rank.Six)
        card4 = Card(Suit.Hearts, Rank.Six)
        card5 = Card(Suit.Spades, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.Six, hand.get_four_of_a_kind())


    def test_get_four_of_a_kind_value_when_there_are_not_four_of_a_kind(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Clubs, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Queen)
        card5 = Card(Suit.Spades, Rank.King)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.NULL, hand.get_four_of_a_kind())

    def test_is_straight(self):
        card1 = Card(Suit.Clubs, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Five)
        card5 = Card(Suit.Spades, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertTrue(hand.is_a_straight())

    def test_is_straight_another_case(self):
        card1 = Card(Suit.Clubs, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Four)
        card3 = Card(Suit.Clubs, Rank.Six)
        card4 = Card(Suit.Hearts, Rank.Eight)
        card5 = Card(Suit.Spades, Rank.Seven)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertTrue(hand.is_a_straight())

    def test_is_not_a_straight(self):
        card1 = Card(Suit.Clubs, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Five)
        card5 = Card(Suit.Spades, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertFalse(hand.is_a_straight())

    def test_is_not_a_straight_another_case(self):
        card1 = Card(Suit.Clubs, Rank.Jack)
        card2 = Card(Suit.Diamonds, Rank.Queen)
        card3 = Card(Suit.Clubs, Rank.King)
        card4 = Card(Suit.Hearts, Rank.Ace)
        card5 = Card(Suit.Spades, Rank.Two)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertFalse(hand.is_a_straight())

    def test_is_flush(self):
        card1 = Card(Suit.Clubs, Rank.Two)
        card2 = Card(Suit.Clubs, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Clubs, Rank.King)
        card5 = Card(Suit.Clubs, Rank.Three)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertTrue(hand.is_a_flush())

    def test_is_not_a_flush(self):
        card1 = Card(Suit.Clubs, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.King)
        card5 = Card(Suit.Clubs, Rank.Three)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertFalse(hand.is_a_flush())

    def test_get_kicker_two_of_a_kind(self):
        card1 = Card(Suit.Clubs, Rank.Eight)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.King)
        card5 = Card(Suit.Clubs, Rank.Three)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.King, hand.get_kicker())

    def test_get_kicker_two_pair(self):
        card1 = Card(Suit.Clubs, Rank.Eight)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Four)
        card5 = Card(Suit.Clubs, Rank.Three)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.Three, hand.get_kicker())

    def test_get_kicker_three_of_a_kind(self):
        card1 = Card(Suit.Clubs, Rank.Eight)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Clubs, Rank.Eight)
        card4 = Card(Suit.Hearts, Rank.King)
        card5 = Card(Suit.Clubs, Rank.Ace)
        hand = Hand(card1, card2, card3, card4, card5)
        self.assertEqual(Rank.Ace, hand.get_kicker())

if __name__ == '__main__':
    unittest.main()