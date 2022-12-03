from unittest import TestCase
from game import check_player_level


class TestCheckPlayerLevel(TestCase):
    def test_check_player_level_not_leveled_up_to_two(self):
        test_player = {
            'level': 1,
            'exp': 2
            }
        self.assertEqual(False, check_player_level(test_player))

    def test_check_player_level_leveled_up_to_two(self):
        test_player = {
            'level': 1,
            'exp': 5
            }
        self.assertEqual(True, check_player_level(test_player))

    def test_check_player_level_not_leveled_up_to_three(self):
        test_player = {
            'level': 2,
            'exp': 7
            }
        self.assertEqual(False, check_player_level(test_player))

    def test_check_player_level_leveled_up_to_three(self):
        test_player = {
            'level': 2,
            'exp': 10
            }
        self.assertEqual(True, check_player_level(test_player))
