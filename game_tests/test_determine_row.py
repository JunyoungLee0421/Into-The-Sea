from unittest import TestCase
from game import determine_row


class TestDetermineRow(TestCase):
    def test_determine_row_level_1(self):
        test_player = {'level': 1}
        self.assertEqual(4, determine_row(test_player))

    def test_determine_row_level_2(self):
        test_player = {'level': 2}
        self.assertEqual(7, determine_row(test_player))

    def test_determine_row_level_3(self):
        test_player = {'level': 3}
        self.assertEqual(7, determine_row(test_player))
