from pokerHands.game.HandType import HandType
from pokerHands.game.HighCard import HighCard
from pokerHands.game.ThreeOfAKind import ThreeOfAKind
from pokerHands.game.TwoOfAKind import TwoOfAKind
from pokerHands.game.TwoPair import TwoPair
from pokerHands.model.Rank import Rank


class HandEvaluator(object):
    def evaluate(self, hand):
        if hand.is_a_straight() and hand.is_a_flush():
            return HandType.Straight_Flush
        elif hand.get_four_of_a_kind() != Rank.NULL:
            return HandType.Four_of_a_Kind
        elif hand.is_a_flush():
            return HandType.Flush
        elif hand.get_three_of_a_kind() != Rank.NULL and len(hand.get_pairs()) > 0:
            return HandType.Full_House
        elif hand.is_a_straight():
            return HandType.Straight
        elif hand.get_three_of_a_kind() != Rank.NULL:
            return ThreeOfAKind()
        elif len(hand.get_pairs()) == 2:
            return TwoPair()
        elif len(hand.get_pairs()) == 1:
            return TwoOfAKind()
        else:
            return HighCard()
