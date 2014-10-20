import os
from unittest.mock import Mock
from pokerHands.euler.HandGenerator import HandGenerator
from pokerHands.euler.LineParser import LineParser
from pokerHands.euler.EulerEvaluator import EulerEvaluator
from pokerHands.game.HandComparator import HandComparator
from pokerHands.game.HandEvaluator import HandEvaluator
from pokerHands.game.Winner import Winner
from pokerHandsTest.euler.EulerHandEvaluatorResource import EulerHanderEvaluatorResource

__author__ = 'Cyrus'

import unittest


class EulerEvaluatorTestCase(unittest.TestCase):
    def test_evaluate_file(self):
        mock_hand_generator = Mock()
        mock_hand_comparator = Mock()

        mock_hand1 = Mock()
        mock_hand2 = Mock()
        mock_hand3 = Mock()
        mock_hand4 = Mock()
        mock_hand5 = Mock()
        mock_hand6 = Mock()
        mock_hand7 = Mock()
        mock_hand8 = Mock()

        values = {0: Winner.Player_One, 1: Winner.Player_Two,
                  2: Winner.Tie, 3: Winner.Player_One}
        self.number_of_times_called = 0

        calls_to_determine_winner = {}

        def mock_determine(hand1, hand2):
            winner = values[self.number_of_times_called]
            calls_to_determine_winner[self.number_of_times_called] = [hand1, hand2]
            self.number_of_times_called += 1
            return winner

        mock_hand_comparator.determine_winner = mock_determine
        mock_hand_generator.parse = Mock(
            return_value=[[mock_hand1, mock_hand2], [mock_hand3, mock_hand4], [mock_hand5, mock_hand6],
                          [mock_hand7, mock_hand8]])

        evaluator = EulerEvaluator(mock_hand_generator, mock_hand_comparator)


        temp_file = open('fake_euler_file.txt','w')
        temp_file.write('line1\n')
        temp_file.write('line2\n')
        temp_file.write('line3\n')
        temp_file.close()
        try:
            result = evaluator.evaluate('fake_euler_file.txt')
            self.assertEqual(2, result.player_one_wins)
            self.assertEqual(1, result.player_two_wins)
            self.assertEqual(1, result.ties)
            self.assertEquals([mock_hand1, mock_hand2], calls_to_determine_winner[0])
            self.assertEquals([mock_hand3, mock_hand4], calls_to_determine_winner[1])
            self.assertEquals([mock_hand5, mock_hand6], calls_to_determine_winner[2])
            self.assertEquals([mock_hand7, mock_hand8], calls_to_determine_winner[3])
            mock_hand_generator.parse.assert_called_with(['line1', 'line2', 'line3'])
        finally:
            os.remove('fake_euler_file.txt')

    def test_functional_euler_evaluation(self):
        evaluator = EulerEvaluator(HandGenerator(LineParser()), HandComparator(HandEvaluator()))
        temp_file = open('euler_hands.txt','w')
        for line in EulerHanderEvaluatorResource.lines():
            temp_file.write(line +"\n")
        temp_file.close()
        try:
            results = evaluator.evaluate('euler_hands.txt')
            self.assertEqual(376, results.player_one_wins)
            self.assertEqual(624, results.player_two_wins)
        finally:
            os.remove('euler_hands.txt')


if __name__ == '__main__':
    unittest.main()
