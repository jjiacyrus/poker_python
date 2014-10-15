from pokerHands.game.FullHouse import FullHouse
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class FullHouseTestCase(unittest.TestCase):
    def test_is_singleton(self):
        self.assertEqual(FullHouse(), FullHouse())

    def test_rank(self):
        self.assertEqual(7, FullHouse().rank)

    def test_resolve_three_of_a_kind_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Nine)
        card4 = Card(Suit.Clubs, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Eight)
        card10 = Card(Suit.Spades, Rank.Eight)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, FullHouse().resolve(hand1, hand2))

    def test_resolve_three_of_a_kind_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Nine)
        card4 = Card(Suit.Clubs, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Jack)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.Jack)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, FullHouse().resolve(hand1, hand2))


    def test_resolve_three_of_a_kind_tie_goes_to_pair_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Nine)
        card4 = Card(Suit.Clubs, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Clubs, Rank.Nine)
        card10 = Card(Suit.Spades, Rank.Nine)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, FullHouse().resolve(hand1, hand2))

    def test_resolve_three_of_a_kind_tie_goes_to_pair_player_two_wins(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Nine)
        card4 = Card(Suit.Clubs, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Eight)
        card7 = Card(Suit.Spades, Rank.Eight)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Clubs, Rank.Nine)
        card10 = Card(Suit.Spades, Rank.Nine)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, FullHouse().resolve(hand1, hand2))



    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Eight)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Hearts, Rank.Nine)
        card4 = Card(Suit.Clubs, Rank.Nine)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Eight)
        card7 = Card(Suit.Spades, Rank.Eight)
        card8 = Card(Suit.Hearts, Rank.Nine)
        card9 = Card(Suit.Clubs, Rank.Nine)
        card10 = Card(Suit.Spades, Rank.Nine)
        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, FullHouse().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
