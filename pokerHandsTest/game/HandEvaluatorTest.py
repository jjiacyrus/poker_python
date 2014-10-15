import unittest
from pokerHands.game.FourOfAKind import FourOfAKind
from pokerHands.game.Flush import Flush
from pokerHands.game.FullHouse import FullHouse
from pokerHands.game.HighCard import HighCard
from pokerHands.game.Straight import Straight
from pokerHands.game.StraightFlush import StraightFlush
from pokerHands.game.ThreeOfAKind import ThreeOfAKind
from pokerHands.game.TwoOfAKind import TwoOfAKind
from pokerHands.game.HandEvaluator import HandEvaluator
from pokerHands.game.TwoPair import TwoPair
from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit


class HandEvaluatorTestCase(unittest.TestCase):
    def setUp(self):
        self.evaluator = HandEvaluator()

    def tearDown(self):
        self.evaluator = None

    def test_evaluate_straight_flush(self):
        card1 = Card(Suit.Diamonds, Rank.Jack)
        card2 = Card(Suit.Diamonds, Rank.Eight)
        card3 = Card(Suit.Diamonds, Rank.Nine)
        card4 = Card(Suit.Diamonds, Rank.Ten)
        card5 = Card(Suit.Diamonds, Rank.Seven)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(StraightFlush(), self.evaluator.evaluate(hand))

    def test_evaluate_full_house(self):
        card1 = Card(Suit.Diamonds, Rank.Jack)
        card2 = Card(Suit.Hearts, Rank.Jack)
        card3 = Card(Suit.Spades, Rank.Jack)
        card4 = Card(Suit.Hearts, Rank.Ten)
        card5 = Card(Suit.Diamonds, Rank.Ten)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(FullHouse(), self.evaluator.evaluate(hand))

    def test_evaluate_four_of_a_kind(self):
        card1 = Card(Suit.Diamonds, Rank.Jack)
        card2 = Card(Suit.Hearts, Rank.Jack)
        card3 = Card(Suit.Clubs, Rank.Jack)
        card4 = Card(Suit.Spades, Rank.Jack)
        card5 = Card(Suit.Diamonds, Rank.Four)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(FourOfAKind(), self.evaluator.evaluate(hand))

    def test_evaluate_flush(self):
        card1 = Card(Suit.Diamonds, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Jack)
        card3 = Card(Suit.Diamonds, Rank.Ten)
        card4 = Card(Suit.Diamonds, Rank.Two)
        card5 = Card(Suit.Diamonds, Rank.Four)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(Flush(), self.evaluator.evaluate(hand))

    def test_evaluate_straight(self):
        card1 = Card(Suit.Spades, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Three)
        card3 = Card(Suit.Diamonds, Rank.Four)
        card4 = Card(Suit.Diamonds, Rank.Five)
        card5 = Card(Suit.Diamonds, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(Straight(), self.evaluator.evaluate(hand))

    def test_evaluate_three_of_a_kind(self):
        card1 = Card(Suit.Spades, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Two)
        card3 = Card(Suit.Spades, Rank.Two)
        card4 = Card(Suit.Diamonds, Rank.Five)
        card5 = Card(Suit.Diamonds, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(ThreeOfAKind(), self.evaluator.evaluate(hand))

    def test_evaluate_two_pair(self):
        card1 = Card(Suit.Spades, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Two)
        card3 = Card(Suit.Spades, Rank.Three)
        card4 = Card(Suit.Diamonds, Rank.Three)
        card5 = Card(Suit.Diamonds, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(TwoPair(), self.evaluator.evaluate(hand))

    def test_evaluate_two_of_a_kind(self):
        card1 = Card(Suit.Spades, Rank.Two)
        card2 = Card(Suit.Diamonds, Rank.Two)
        card3 = Card(Suit.Spades, Rank.Three)
        card4 = Card(Suit.Diamonds, Rank.Five)
        card5 = Card(Suit.Diamonds, Rank.Six)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(TwoOfAKind(), self.evaluator.evaluate(hand))

    def test_high_card(self):
        card1 = Card(Suit.Hearts, Rank.Ace)
        card2 = Card(Suit.Diamonds, Rank.Two)
        card3 = Card(Suit.Spades, Rank.Four)
        card4 = Card(Suit.Diamonds, Rank.Ten)
        card5 = Card(Suit.Diamonds, Rank.Jack)
        hand = Hand(card1, card2, card3, card4, card5)

        self.assertEqual(HighCard(), self.evaluator.evaluate(hand))


if __name__ == '__main__':
    unittest.main()