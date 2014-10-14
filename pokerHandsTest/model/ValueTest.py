__author__ = 'Cyrus'

import unittest
from pokerHands.model.Value import Value


class ValueTestCase(unittest.TestCase):
    def test_enum_values(self):
        self.assertEqual(Value.NULL.value, 0)
        self.assertEqual(Value.Two.value, 2)
        self.assertEqual(Value.Three.value, 3)
        self.assertEqual(Value.Four.value, 4)
        self.assertEqual(Value.Five.value, 5)
        self.assertEqual(Value.Six.value, 6)
        self.assertEqual(Value.Seven.value, 7)
        self.assertEqual(Value.Eight.value, 8)
        self.assertEqual(Value.Nine.value, 9)
        self.assertEqual(Value.Ten.value, 10)
        self.assertEqual(Value.Jack.value, 11)
        self.assertEqual(Value.Queen.value, 12)
        self.assertEqual(Value.King.value, 13)
        self.assertEqual(Value.Ace.value, 14)

    def test_find_by_abbreviation(self):
        self.assertEqual(Value.Two, Value.find('2'))
        self.assertEqual(Value.Three, Value.find('3'))
        self.assertEqual(Value.Four, Value.find('4'))
        self.assertEqual(Value.Five, Value.find('5'))
        self.assertEqual(Value.Six, Value.find('6'))
        self.assertEqual(Value.Seven, Value.find('7'))
        self.assertEqual(Value.Eight, Value.find('8'))
        self.assertEqual(Value.Nine, Value.find('9'))
        self.assertEqual(Value.Ten, Value.find('10'))
        self.assertEqual(Value.Jack, Value.find('J'))
        self.assertEqual(Value.Queen, Value.find('Q'))
        self.assertEqual(Value.King, Value.find('K'))
        self.assertEqual(Value.Ace, Value.find('A'))
        self.assertEqual(Value.NULL, Value.find('D'))

