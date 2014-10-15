from pokerHands.Singleton import singleton
from pokerHands.game.HighCard import HighCard

__author__ = 'Cyrus'


@singleton
class StraightFlush(object):
    def __init__(self):
        self.rank = 9

    def resolve(self, hand1, hand2):
        return HighCard().resolve(hand1, hand2)
