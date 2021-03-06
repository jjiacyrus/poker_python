from pokerHands.game.FourOfAKind import FourOfAKind
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class FourOfAKindTestCase(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(FourOfAKind(), FourOfAKind())

    def test_rank(self):
        self.assertEqual(8, FourOfAKind().rank)

    def test_resolve_by_rank_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Five)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Four)
        card9 = Card(Suit.Clubs, Rank.Four)
        card10 = Card(Suit.Spades, Rank.Two)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, FourOfAKind().resolve(hand1, hand2))

    def test_resolve_by_rank_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Five)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Jack)
        card7 = Card(Suit.Spades, Rank.Jack)
        card8 = Card(Suit.Hearts, Rank.Jack)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.Two)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, FourOfAKind().resolve(hand1, hand2))

    def test_resolve_by_kicker_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Jack)
        card2 = Card(Suit.Diamonds, Rank.Jack)
        card3 = Card(Suit.Hearts, Rank.Jack)
        card4 = Card(Suit.Clubs, Rank.Jack)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Jack)
        card7 = Card(Suit.Spades, Rank.Jack)
        card8 = Card(Suit.Hearts, Rank.Jack)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.Two)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, FourOfAKind().resolve(hand1, hand2))

    def test_resolve_by_kicker_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Jack)
        card2 = Card(Suit.Diamonds, Rank.Jack)
        card3 = Card(Suit.Hearts, Rank.Jack)
        card4 = Card(Suit.Clubs, Rank.Jack)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Jack)
        card7 = Card(Suit.Spades, Rank.Jack)
        card8 = Card(Suit.Hearts, Rank.Jack)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.Ace)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, FourOfAKind().resolve(hand1, hand2))

    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Jack)
        card2 = Card(Suit.Diamonds, Rank.Jack)
        card3 = Card(Suit.Hearts, Rank.Jack)
        card4 = Card(Suit.Clubs, Rank.Jack)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Jack)
        card7 = Card(Suit.Spades, Rank.Jack)
        card8 = Card(Suit.Hearts, Rank.Jack)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.Nine)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, FourOfAKind().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
