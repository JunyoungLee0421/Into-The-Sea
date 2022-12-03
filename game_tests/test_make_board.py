from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_smallest_board(self):
        expected = {(0, 0): 'empty_room'}
        self.assertEqual(expected, make_board(1, 1))

    def test_make_board_random_size(self):
        expected = {(0, 0): 'empty_room', (0, 1): 'empty_room', (0, 2): 'empty_room', (1, 0): 'empty_room',
                    (1, 1): 'empty_room', (1, 2): 'empty_room', (2, 0): 'empty_room', (2, 1): 'empty_room',
                    (2, 2): 'empty_room'}
        self.assertEqual(expected, make_board(3, 3))

    def test_make_board_non_square(self):
        expected = {(0, 0): 'empty_room', (0, 1): 'empty_room'}
        self.assertEqual(expected, make_board(1, 2))
