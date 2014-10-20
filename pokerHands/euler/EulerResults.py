__author__ = 'Cyrus'


class EulerResults(object):
    def __init__(self, player_one_wins, player_two_wins, ties):
        self.player_one_wins = player_one_wins
        self.player_two_wins = player_two_wins
        self.ties = ties
