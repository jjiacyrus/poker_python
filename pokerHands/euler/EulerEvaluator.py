from pokerHands.euler.EulerResults import EulerResults
from pokerHands.game.Winner import Winner


class EulerEvaluator(object):
    def __init__(self, hand_generator, hand_comparator):
        self.hand_generator = hand_generator
        self.hand_comparator = hand_comparator

    @staticmethod
    def __get_euler_lines(open_file):
        lines = []
        for line in open_file:
            lines.append(line.rstrip())
        return lines

    def __evaluate_lines(self, hand_pairs, player_one_wins, player_two_wins, ties):
        for pair in hand_pairs:
            winner = self.hand_comparator.determine_winner(pair[0], pair[1])
            if winner == Winner.Player_One:
                player_one_wins += 1
            elif winner == Winner.Player_Two:
                player_two_wins += 1
            else:
                ties += 1
        return EulerResults(player_one_wins, player_two_wins, ties)

    def evaluate(self, file):
        with open(file) as open_file:
            player_one_wins = 0
            player_two_wins = 0
            ties = 0
            lines = self.__get_euler_lines(open_file)
            hand_pairs = self.hand_generator.parse(lines)
            return self.__evaluate_lines(hand_pairs, player_one_wins, player_two_wins, ties)




