from pokerHands.game.Flush import Flush
from pokerHands.game.FourOfAKind import FourOfAKind
from pokerHands.game.FullHouse import FullHouse
from pokerHands.game.HighCard import HighCard
from pokerHands.game.Straight import Straight
from pokerHands.game.StraightFlush import StraightFlush
from pokerHands.game.ThreeOfAKind import ThreeOfAKind
from pokerHands.game.TwoOfAKind import TwoOfAKind
from pokerHands.game.TwoPair import TwoPair
from pokerHands.model.Rank import Rank


class HandEvaluator(object):
    def evaluate(self, hand):
        if hand.is_a_straight() and hand.is_a_flush():
            return StraightFlush()
        elif hand.get_four_of_a_kind() != Rank.NULL:
            return FourOfAKind()
        elif hand.get_three_of_a_kind() != Rank.NULL and len(hand.get_pairs()) > 0:
            return FullHouse()
        elif hand.is_a_flush():
            return Flush()
        elif hand.is_a_straight():
            return Straight()
        elif hand.get_three_of_a_kind() != Rank.NULL:
            return ThreeOfAKind()
        elif len(hand.get_pairs()) == 2:
            return TwoPair()
        elif len(hand.get_pairs()) == 1:
            return TwoOfAKind()
        else:
            return HighCard()
