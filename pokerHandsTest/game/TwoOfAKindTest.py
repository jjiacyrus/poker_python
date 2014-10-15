from pokerHands.game.TwoOfAKind import TwoOfAKind
from pokerHands.game.Winner import Winner
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

import unittest


class TwoOfAKindTestCase(unittest.TestCase):
    def test_is_a_singleton(self):
        self.assertEquals(TwoOfAKind(), TwoOfAKind())

    def test_rank(self):
        self.assertEquals(2, TwoOfAKind().rank)

    def test_break_two_of_a_kind(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Five)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.King)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_Two, TwoOfAKind().resolve(hand1, hand2))

    def test_break_two_of_a_kind_player_one_wins(self):
        card1 = Card(Suit.Hearts, Rank.Ten)
        card2 = Card(Suit.Diamonds, Rank.Ten)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Nine)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Five)
        card7 = Card(Suit.Spades, Rank.Five)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.King)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, TwoOfAKind().resolve(hand1, hand2))

    def test_break_two_of_a_kind_equal_ranks_goes_to_the_kicker(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Ace)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Spades, Rank.King)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Player_One, TwoOfAKind().resolve(hand1, hand2))

    def test_break_two_of_a_kind_equal_ranks_with_equal_kicker(self):
        card1 = Card(Suit.Hearts, Rank.Four)
        card2 = Card(Suit.Diamonds, Rank.Four)
        card3 = Card(Suit.Hearts, Rank.Five)
        card4 = Card(Suit.Clubs, Rank.Seven)
        card5 = Card(Suit.Spades, Rank.Ace)

        hand1 = Hand(card1, card2, card3, card4, card5)

        card6 = Card(Suit.Clubs, Rank.Four)
        card7 = Card(Suit.Spades, Rank.Four)
        card8 = Card(Suit.Hearts, Rank.Eight)
        card9 = Card(Suit.Clubs, Rank.Jack)
        card10 = Card(Suit.Diamonds, Rank.Ace)

        hand2 = Hand(card6, card7, card8, card9, card10)

        self.assertEqual(Winner.Tie, TwoOfAKind().resolve(hand1, hand2))


if __name__ == '__main__':
    unittest.main()
