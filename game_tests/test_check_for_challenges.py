from unittest import TestCase
from game import check_for_challenges


class TestCheckForChallenges(TestCase):
    def test_check_for_challenges_level_one_event(self):
        test_player = {'row': 1, 'column': 3}
        test_board = {(1, 3): 'level_one_event'}
        self.assertEqual(True, check_for_challenges(test_board, test_player))

    def test_check_for_challenges_level_two_event(self):
        test_player = {'row': 5, 'column': 1}
        test_board = {(5, 1): 'level_two_event'}
        self.assertEqual(True, check_for_challenges(test_board, test_player))

    def test_check_for_challenges_level_three_event(self):
        test_player = {'row': 7, 'column': 3}
        test_board = {(7, 3): 'level_three_event'}
        self.assertEqual(True, check_for_challenges(test_board, test_player))

    def test_check_for_challenges_octopus_event(self):
        test_player = {'row': 8, 'column': 9}
        test_board = {(8, 9): 'octopus_event'}
        self.assertEqual(True, check_for_challenges(test_board, test_player))

    def test_check_for_challenges_empty_room(self):
        test_player = {'row': 0, 'column': 0}
        test_board = {(0, 0): 'empty_room'}
        self.assertEqual(False, check_for_challenges(test_board, test_player))
