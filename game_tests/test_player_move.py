from unittest import TestCase
from game import player_move


class TestPlayerMove(TestCase):
    def test_player_move_north(self):
        test_player = {'row': 1, 'column': 1}
        test_input = '1'
        expected = {'row': 0, 'column': 1}
        self.assertEqual(expected, player_move(test_player, test_input))

    def test_player_move_south(self):
        test_player = {'row': 1, 'column': 1}
        test_input = '2'
        expected = {'row': 2, 'column': 1}
        self.assertEqual(expected, player_move(test_player, test_input))

    def test_player_move_east(self):
        test_player = {'row': 1, 'column': 1}
        test_input = '3'
        expected = {'row': 1, 'column': 2}
        self.assertEqual(expected, player_move(test_player, test_input))

    def test_player_move_west(self):
        test_player = {'row': 1, 'column': 1}
        test_input = '4'
        expected = {'row': 1, 'column': 0}
        self.assertEqual(expected, player_move(test_player, test_input))
