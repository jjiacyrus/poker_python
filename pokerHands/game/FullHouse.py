from pokerHands.Singleton import singleton
from pokerHands.game.Winner import Winner

__author__ = 'Cyrus'


@singleton
class FullHouse(object):
    def __init__(self):
        self.rank = 7

    def resolve(self, hand1, hand2):
        if hand1.get_three_of_a_kind() > hand2.get_three_of_a_kind():
            return Winner.Player_One
        elif hand1.get_three_of_a_kind() < hand2.get_three_of_a_kind():
            return Winner.Player_Two
        else:
            return self.__evaluate_pair(hand1, hand2)

    def __evaluate_pair(self, hand1, hand2):
        if hand1.get_pairs()[0] > hand2.get_pairs()[0]:
            return Winner.Player_One
        elif hand1.get_pairs()[0] < hand2.get_pairs()[0]:
            return Winner.Player_Two
        else:
            return Winner.Tie

