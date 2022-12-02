import io
from unittest import TestCase
from unittest.mock import patch
from game import stats


class TestStats(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_Patty(self, mock_output):
        test_player = {'name': 'Patty', 'sub_name': 'Happy', 'row': 0, 'column': 0, 'level': 1, 'exp': 0,
                       'morale': 3, 'hp': 100, 'attack': 20}
        stats(test_player)
        game_print = mock_output.getvalue()
        expected = "Patty captain of the Happy\n" "Level: 1\n""Exp: 0\n""Morale: 3\n""Battle HP: 100\n""Attack: 20\n"
        self.assertEqual(expected, game_print)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_stats_Tim(self, mock_output):
        test_player = {'name': 'Tim', 'sub_name': 'Energized', 'row': 10, 'column': 10, 'level': 3, 'exp': 9,
                       'morale': 8, 'hp': 200, 'attack': 50}
        stats(test_player)
        game_print = mock_output.getvalue()
        expected = "Tim captain of the Energized\n" "Level: 3\n""Exp: 9\n""Morale: 8\n""Battle HP: 200\n""Attack: 50\n"
        self.assertEqual(expected, game_print)