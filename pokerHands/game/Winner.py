__author__ = 'Cyrus'
from enum import Enum,unique
@unique
class Winner(Enum):
    Tie = 0
    Player_One = 1
    Player_Two = 2