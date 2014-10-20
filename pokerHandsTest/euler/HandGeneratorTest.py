from unittest.mock import Mock
from pokerHands.euler.HandGenerator import HandGenerator

__author__ = 'Cyrus'

import unittest


class HandGeneratorTestCase(unittest.TestCase):
    def test_generate_hands(self):
        line1 = 'abc'
        line2 = 'def'
        line3 = 'ghi'

        mock_hand1 = Mock()
        mock_hand2 = Mock()
        mock_hand3 = Mock()
        mock_hand4 = Mock()
        mock_hand5 = Mock()
        mock_hand6 = Mock()

        values = {line1: [mock_hand1, mock_hand2], line2: [mock_hand3, mock_hand4], line3: [mock_hand5, mock_hand6]}

        def mock_parse(line):
            return values[line]

        mock_line_parser = Mock()
        mock_line_parser.parse = mock_parse

        generator = HandGenerator(mock_line_parser)

        self.assertEqual([[mock_hand1, mock_hand2], [mock_hand3, mock_hand4], [mock_hand5, mock_hand6]],
                         generator.parse([line1, line2, line3]))


if __name__ == '__main__':
    unittest.main()
