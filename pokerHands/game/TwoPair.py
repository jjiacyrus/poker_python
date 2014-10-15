from pokerHands.Singleton import singleton
from pokerHands.game.HighCard import HighCard
from pokerHands.game.Winner import Winner


@singleton
class TwoPair(object):
    def __init__(self):
        self.rank = 3

    def resolve(self, hand1, hand2):
        if hand1.get_pairs()[1] > hand2.get_pairs()[1]:
            return Winner.Player_One
        elif hand1.get_pairs()[1] < hand2.get_pairs()[1]:
            return Winner.Player_Two
        else:
            return self.__evaluate_secondary_rank(hand1, hand2)

    def __evaluate_secondary_rank(self, hand1, hand2):
        if hand1.get_pairs()[0] > hand2.get_pairs()[0]:
            return Winner.Player_One
        elif hand1.get_pairs()[0] < hand2.get_pairs()[0]:
            return Winner.Player_Two
        else:
            return HighCard().resolve(hand1, hand2)

