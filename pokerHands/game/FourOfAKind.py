from pokerHands.Singleton import singleton
from pokerHands.game.HighCard import HighCard
from pokerHands.game.Winner import Winner


@singleton
class FourOfAKind(object):
    def __init__(self):
        self.rank = 8

    def resolve(self, hand1, hand2):
        if hand1.get_four_of_a_kind() > hand2.get_four_of_a_kind():
            return Winner.Player_One
        elif hand1.get_four_of_a_kind() < hand2.get_four_of_a_kind():
            return Winner.Player_Two
        else:
            return HighCard().resolve(hand1, hand2)


