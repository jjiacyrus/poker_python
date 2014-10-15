from pokerHands.game.ThreeOfAKind import ThreeOfAKind
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class ThreeOfAKindTestCase(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(ThreeOfAKind(), ThreeOfAKind())

    def test_rank(self):
        self.assertEqual(4, ThreeOfAKind().rank)

    def test_resolve_by_rank_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Four)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, ThreeOfAKind().resolve(hand1, hand2))

    def test_resolve_by_rank_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Five)
        card2 = Card(Suit.Diamonds, Rank.Five)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Ten)
        card7 = Card(Suit.Spades, Rank.Ten)
        card8 = Card(Suit.Hearts, Rank.Ten)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, ThreeOfAKind().resolve(hand1, hand2))

    def test_rank_tie_resolves_with_kicker_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Ten)
        card2 = Card(Suit.Diamonds, Rank.Ten)
        card3 = Card(Suit.Hearts, Rank.Ten)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Ten)
        card7 = Card(Suit.Spades, Rank.Ten)
        card8 = Card(Suit.Hearts, Rank.Ten)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Two)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, ThreeOfAKind().resolve(hand1, hand2))

    def test_rank_tie_resolves_with_kicker_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Ten)
        card2 = Card(Suit.Diamonds, Rank.Ten)
        card3 = Card(Suit.Hearts, Rank.Ten)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Ten)
        card7 = Card(Suit.Spades, Rank.Ten)
        card8 = Card(Suit.Hearts, Rank.Ten)
        card9 = Card(Suit.Clubs, Rank.Three)
        card10 = Card(Suit.Spades, Rank.Jack)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, ThreeOfAKind().resolve(hand1, hand2))
if __name__ == '__main__':
    unittest.main()
