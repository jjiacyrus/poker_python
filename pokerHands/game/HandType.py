__author__ = 'Cyrus'
from enum import Enum,unique
@unique
class HandType(Enum):
    High_Card = 1
    Two_of_a_Kind = 2
    Two_Pair = 3
    Three_of_a_Kind = 4
    Straight = 5
    Flush = 6
    Full_House = 7
    Four_of_a_Kind = 8
    Straight_Flush = 9
