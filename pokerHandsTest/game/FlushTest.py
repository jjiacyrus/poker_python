from pokerHands.game.Flush import Flush
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class FlushTestCase(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(Flush(), Flush())

    def test_rank(self):
        self.assertEqual(6, Flush().rank)

    def test_resolve_player_one_has_higher_top_card(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Eight)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Flush().resolve(hand1, hand2))

    def test_resolve_player_two_has_higher_top_card(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Ten)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Flush().resolve(hand1, hand2))

    def test_resolve_tied_top_card_goes_to_secondary_card_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Six)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Flush().resolve(hand1, hand2))

    def test_resolve_tied_top_card_goes_to_secondary_card_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Six)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Flush().resolve(hand1, hand2))

    def test_resolve_third_card_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Three)
        card8 = Card(Suit.Diamonds, Rank.Four)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Flush().resolve(hand1, hand2))

    def test_resolve_third_card_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Three)
        card3 = Card(Suit.Hearts, Rank.Four)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Three)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Flush().resolve(hand1, hand2))

    def test_resolve_fourth_card_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Three)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Flush().resolve(hand1, hand2))

    def test_resolve_fourth_card_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Three)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Flush().resolve(hand1, hand2))

    def test_resolve_fifth_card_player_one(self):
        card1 = Card(Suit.Hearts, Rank.Three)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, Flush().resolve(hand1, hand2))

    def test_resolve_fifth_card_player_two(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Three)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, Flush().resolve(hand1, hand2))

    def test_resolve_tie(self):
        card1 = Card(Suit.Hearts, Rank.Two)
        card2 = Card(Suit.Hearts, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Hearts, Rank.Seven)
        card5 = Card(Suit.Hearts, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Diamonds, Rank.Two)
        card7 = Card(Suit.Diamonds, Rank.Four)
        card8 = Card(Suit.Diamonds, Rank.Five)
        card9 = Card(Suit.Diamonds, Rank.Seven)
        card10 = Card(Suit.Diamonds, Rank.Nine)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, Flush().resolve(hand1, hand2))
        

if __name__ == '__main__':
    unittest.main()
