from pokerHands.Singleton import singleton
from pokerHands.game.HighCard import HighCard
from pokerHands.game.Winner import Winner

__author__ = 'Cyrus'


@singleton
class ThreeOfAKind(object):
    def __init__(self):
        self.rank = 4

    def resolve(self, hand1, hand2):
        if hand1.get_three_of_a_kind() > hand2.get_three_of_a_kind():
            return Winner.Player_One
        elif hand1.get_three_of_a_kind() < hand2.get_three_of_a_kind():
            return Winner.Player_Two
        else:
            return HighCard().resolve(hand1,hand2)
