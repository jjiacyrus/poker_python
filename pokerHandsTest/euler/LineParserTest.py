from pokerHands.euler.LineParser import LineParser
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'

import unittest


class LineParserTestCase(unittest.TestCase):
    def test_parse_line(self):
        parser = LineParser()
        hands = parser.parse("8C TS KC 9H 4S 7D 2S 5D 3S AC")
        self.assertEqual(2, len(hands))
        hand1 = hands[0]
        self.__check_card_at_index(hand1, 0, Rank.Four, Suit.Spades)
        self.__check_card_at_index(hand1, 1, Rank.Eight, Suit.Clubs)
        self.__check_card_at_index(hand1, 2, Rank.Nine, Suit.Hearts)
        self.__check_card_at_index(hand1, 3, Rank.Ten, Suit.Spades)
        self.__check_card_at_index(hand1, 4, Rank.King, Suit.Clubs)

        hand2 = hands[1]
        self.__check_card_at_index(hand2, 0, Rank.Two, Suit.Spades)
        self.__check_card_at_index(hand2, 1, Rank.Three, Suit.Spades)
        self.__check_card_at_index(hand2, 2, Rank.Five, Suit.Diamonds)
        self.__check_card_at_index(hand2, 3, Rank.Seven, Suit.Diamonds)
        self.__check_card_at_index(hand2, 4, Rank.Ace, Suit.Clubs)

    def __check_card_at_index(self, hand, index, expected_rank, expected_suit):
        self.assertEqual(expected_rank, hand.cards[index].rank)
        self.assertEqual(expected_suit, hand.cards[index].suit)


if __name__ == '__main__':
    unittest.main()
