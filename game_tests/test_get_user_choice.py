from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=[1])
    def test_get_user_choice_number(self, _):
        test_player = {'level': 1}
        self.assertEqual(1, get_user_choice(test_player))

    @patch('builtins.input', side_effect=['s'])
    def test_get_user_choice_letter(self, _):
        test_player = {'level': 3}
        self.assertEqual('s', get_user_choice(test_player))
