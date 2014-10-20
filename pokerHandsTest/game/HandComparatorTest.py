from pokerHands.game.HandEvaluator import HandEvaluator
from pokerHands.game.HandComparator import HandComparator
from pokerHands.game.Winner import Winner

__author__ = 'Cyrus'

import unittest
from unittest.mock import MagicMock, Mock, PropertyMock


class HandComparatorTestCase(unittest.TestCase):
    def test_evaluate_hands_and_compares_ranks_hand1_wins(self):
        mock_result_1 = Mock()
        mock_result_1.rank = 12
        mock_result_2 = Mock()
        mock_result_2.rank = 8

        mock_hand1 = Mock()
        mock_hand2 = Mock()

        values = {mock_hand1: mock_result_1, mock_hand2: mock_result_2}

        def mock_evaluate(hand):
            return values[hand]

        mock_evaluator = Mock()
        mock_evaluator.evaluate = mock_evaluate

        comparator = HandComparator(mock_evaluator)

        self.assertEqual(Winner.Player_One, comparator.determine_winner(mock_hand1, mock_hand2))

    def test_evaluate_hands_and_compares_ranks_hand2_wins(self):
        mock_result_1 = Mock()
        mock_result_1.rank = 12
        mock_result_2 = Mock()
        mock_result_2.rank = 18

        mock_hand1 = Mock()
        mock_hand2 = Mock()

        values = {mock_hand1: mock_result_1, mock_hand2: mock_result_2}

        def evaluate(hand):
            return values[hand]

        mock_evaluator = Mock()
        mock_evaluator.evaluate = evaluate

        comparator = HandComparator(mock_evaluator)

        self.assertEqual(Winner.Player_Two, comparator.determine_winner(mock_hand1, mock_hand2))

    def test_evaluate_hands_with_equal_ranks_will_ask_result_to_resolve_winner(self):
        mock_result_1 = Mock()
        mock_result_1.rank = 12
        mock_result_2 = Mock()
        mock_result_2.rank = 12

        mock_hand1 = Mock()
        mock_hand2 = Mock()

        values = {mock_hand1: mock_result_1, mock_hand2: mock_result_2}

        mock_result_1.resolve = Mock(return_value=Winner.Player_One)

        def evaluate(hand):
            return values[hand]

        mock_evaluator = Mock()
        mock_evaluator.evaluate = evaluate

        comparator = HandComparator(mock_evaluator)

        self.assertEqual(Winner.Player_One, comparator.determine_winner(mock_hand1, mock_hand2))
        mock_result_1.resolve.assert_called_with(mock_hand1, mock_hand2)

if __name__ == '__main__':
    unittest.main()
