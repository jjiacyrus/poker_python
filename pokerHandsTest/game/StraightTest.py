from pokerHands.game.Straight import Straight
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class StraightTestCase(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(Straight(), Straight())

    def test_rank(self):
        self.assertEqual(5, Straight().rank)

    def test_resolve_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Clubs, Rank.Eight)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Five)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Clubs, Rank.Seven)
        card10 = Card(Suit.Spades, Rank.Eight)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Straight().resolve(hand1, hand2))

    def test_resolve_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Clubs, Rank.Eight)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Ten)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Clubs, Rank.Seven)
        card10 = Card(Suit.Spades, Rank.Eight)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Straight().resolve(hand1, hand2))

    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Six)
        card3 = Card(Suit.Hearts, Rank.Seven)
        card4 = Card(Suit.Clubs, Rank.Eight)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Six)
        card9 = Card(Suit.Clubs, Rank.Seven)
        card10 = Card(Suit.Spades, Rank.Eight)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, Straight().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
