__author__ = 'Cyrus'
from enum import Enum, unique
@unique
class Rank(Enum):
    NULL = 0;
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __lt__(self, other):
        return self.value < other.value


    @staticmethod
    def find(abbreviation):
        if abbreviation == '2':
            return Rank.Two
        elif abbreviation == '3':
            return Rank.Three
        elif abbreviation == '4':
            return Rank.Four
        elif abbreviation == '5':
            return Rank.Five
        elif abbreviation == '6':
            return Rank.Six
        elif abbreviation == '7':
            return Rank.Seven
        elif abbreviation == '8':
            return Rank.Eight
        elif abbreviation == '9':
            return Rank.Nine
        elif abbreviation == 'T':
            return Rank.Ten
        elif abbreviation == 'J':
            return Rank.Jack
        elif abbreviation == 'Q':
            return Rank.Queen
        elif abbreviation == 'K':
            return Rank.King
        elif abbreviation == 'A':
            return Rank.Ace
        else:
            return Rank.NULL
