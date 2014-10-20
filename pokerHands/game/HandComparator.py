from pokerHands.game.Winner import Winner


class HandComparator(object):
    def __init__(self, hand_evaluator):
        self.__hand_evaluator = hand_evaluator

    def determine_winner(self, hand1, hand2):
        hand1_result = self.__hand_evaluator.evaluate(hand1)
        hand2_result = self.__hand_evaluator.evaluate(hand2)

        if hand1_result.rank > hand2_result.rank:
            return Winner.Player_One
        elif hand1_result.rank < hand2_result.rank:
            return Winner.Player_Two
        else:
            return hand1_result.resolve(hand1, hand2)

