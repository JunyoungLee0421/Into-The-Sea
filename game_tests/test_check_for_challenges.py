from unittest import TestCase
from game import check_for_challenges


class TestCheckForChallenges(TestCase):
    def test_check_for_challenges_True(self):
        test_player = {'row': 0, 'column': 0}
        test_board = {(0, 0): 'level_one_event'}
        self.assertEqual(True, check_for_challenges(test_board, test_player))

    def test_check_for_challenges_False(self):
        test_player = {'row': 0, 'column': 0}
        test_board = {(0, 0): 'empty_room'}
        self.assertEqual(False, check_for_challenges(test_board, test_player))

