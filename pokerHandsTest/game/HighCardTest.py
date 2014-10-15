from pokerHands.game.HighCard import HighCard
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class HighCardTestCase(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(HighCard(), HighCard())

    def test_rank(self):
        self.assertEquals(1, HighCard().rank)

    def test_resolve_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, HighCard().resolve(hand1, hand2))

    def test_resolve_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Ace)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, HighCard().resolve(hand1, hand2))

    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, HighCard().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
