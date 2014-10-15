from pokerHands.Singleton import singleton
from pokerHands.game.Winner import Winner


@singleton
class Flush(object):
    def __init__(self):
        self.rank = 6


    def resolve(self, hand1, hand2):
        index = 4
        result = Winner.Tie
        while index >= 0 and result == Winner.Tie:
            result = self.__compare_cards_at_index(index, hand1, hand2)
            index -= 1
        return result

    def __compare_cards_at_index(self, index, hand1, hand2):
        if hand1.cards[index].rank > hand2.cards[index].rank:
            return Winner.Player_One
        elif hand1.cards[index].rank < hand2.cards[index].rank:
            return Winner.Player_Two
        else:
            return Winner.Tie