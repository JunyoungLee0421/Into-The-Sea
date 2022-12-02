import io
from unittest import TestCase
from unittest.mock import patch
from game import sonar


class TestSonar(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_same_row_same_column(self, mock_output):
        test_game_board = {(0, 0): 'octopus_event'}
        test_player = {'row': 0, 'column': 0}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "You're in the same row as the octopus\n" "You're in the same column as the octopus\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_south_of_octopus_row_same_column(self, mock_output):
        test_game_board = {(9, 7): 'octopus_event'}
        test_player = {'row': 10, 'column': 7}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "The octopus is to the North of you\n" "You're in the same column as the octopus\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_north_of_octopus_row_same_column(self, mock_output):
        test_game_board = {(9, 7): 'octopus_event'}
        test_player = {'row': 8, 'column': 7}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "The octopus is to the South of you\n" "You're in the same column as the octopus\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_same_row_west_of_octopus_column(self, mock_output):
        test_game_board = {(9, 7): 'octopus_event'}
        test_player = {'row': 9, 'column': 6}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "You're in the same row as the octopus\n" "The octopus is to the East of you\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_same_row_east_of_octopus_column(self, mock_output):
        test_game_board = {(9, 7): 'octopus_event'}
        test_player = {'row': 9, 'column': 8}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "You're in the same row as the octopus\n" "The octopus is to the West of you\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_sonar_different_row_different_column(self, mock_output):
        test_game_board = {(9, 7): 'octopus_event'}
        test_player = {'row': 5, 'column': 9}
        sonar(test_player, test_game_board)
        game_print = mock_output.getvalue()
        expected = "The octopus is to the South of you\n" "The octopus is to the West of you\n"
        self.assertEqual(expected, game_print)
