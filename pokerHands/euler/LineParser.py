from pokerHands.model.Card import Card
from pokerHands.model.Hand import Hand
from pokerHands.model.Rank import Rank
from pokerHands.model.Suit import Suit

__author__ = 'Cyrus'


class LineParser(object):
    def parse(self, euler_line):
        values = euler_line.split(' ')
        cards = []

        for value in values:
            rank = Rank.find(value[0])
            suit = Suit.find(value[1])
            cards.append(Card(suit, rank))
        hand1 = Hand(cards[0], cards[1], cards[2], cards[3], cards[4])
        hand2 = Hand(cards[5], cards[6], cards[7], cards[8], cards[9])
        return [hand1, hand2]
