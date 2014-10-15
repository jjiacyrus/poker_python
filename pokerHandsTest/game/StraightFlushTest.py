from pokerHands.game.StraightFlush import StraightFlush
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class StraightFlushTestCase(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(StraightFlush(), StraightFlush())

    def test_rank(self):
        self.assertEqual(9, StraightFlush().rank)

    def test_resolve_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Hearts, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Hearts, Rank.Eight)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Hearts, Rank.Four)
        card7 = Card(Suit.Hearts, Rank.Five)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Hearts, Rank.Seven)
        card10 = Card(Suit.Hearts, Rank.Eight)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, StraightFlush().resolve(hand1, hand2))

    def test_resolve_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Hearts, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Hearts, Rank.Eight)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Hearts, Rank.Nine)
        card7 = Card(Suit.Hearts, Rank.Eight)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Hearts, Rank.Seven)
        card10 = Card(Suit.Hearts, Rank.Ten)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, StraightFlush().resolve(hand1, hand2))

    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Hearts, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Hearts, Rank.Eight)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Hearts, Rank.Nine)
        card7 = Card(Suit.Hearts, Rank.Eight)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Hearts, Rank.Seven)
        card10 = Card(Suit.Hearts, Rank.Five)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, StraightFlush().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
