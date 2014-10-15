from pokerHands.game.TwoPair import TwoPair
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class TwoPairTestCase(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(TwoPair(), TwoPair())

    def test_rank(self):
        self.assertEqual(3, TwoPair().rank)

    def test_resolve_player_one_wins_high_rank(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Eight)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Spades, Rank.Five)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, TwoPair().resolve(hand1, hand2))

    def test_resolve_player_two_wins_high_rank(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Ace)
        card8 = Card(Suit.Hearts, Rank.Ace)
        card9 = Card(Suit.Spades, Rank.Five)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, TwoPair().resolve(hand1, hand2))

    def test_resolve_high_rank_tie_falls_back_to_secondary_rank_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Three)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Spades, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, TwoPair().resolve(hand1, hand2))

    def test_resolve_high_rank_tie_falls_back_to_secondary_rank_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Six)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Spades, Rank.Six)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, TwoPair().resolve(hand1, hand2))

    def test_resolve_secondary_rank_tie_falls_back_to_kicker_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Spades, Rank.Five)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, TwoPair().resolve(hand1, hand2))


    def test_resolve_secondary_rank_tie_falls_back_to_kicker_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Spades, Rank.Five)
        card10 = Card(Suit.Spades, Rank.Ace)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, TwoPair().resolve(hand1, hand2))

    def test_resolve_absolute_tie(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Nine)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Two)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Nine)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Spades, Rank.Five)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, TwoPair().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
