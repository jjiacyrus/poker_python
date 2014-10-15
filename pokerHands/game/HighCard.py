from pokerHands.Singleton import singleton
from pokerHands.game.Winner import Winner

__author__ = 'Cyrus'


@singleton
class HighCard(object):
    def __init__(self):
        self.rank = 1

    def resolve(self, hand1, hand2):
        if hand1.get_kicker() > hand2.get_kicker():
            return Winner.Player_One
        elif hand1.get_kicker() < hand2.get_kicker():
            return Winner.Player_Two
        else:
            return Winner.Tie