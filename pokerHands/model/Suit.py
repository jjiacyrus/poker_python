from enum import Enum, unique


@unique
class Suit(Enum):
    NULL = 0
    Clubs = 1
    Spades = 2
    Hearts = 3
    Diamonds = 4


    @staticmethod
    def find(abbreviation):
        if abbreviation == 'S':
            return Suit.Spades
        elif abbreviation == 'C':
            return Suit.Clubs
        elif abbreviation == 'H':
            return Suit.Hearts
        elif abbreviation == 'D':
            return Suit.Diamonds
        else:
            return Suit.NULL