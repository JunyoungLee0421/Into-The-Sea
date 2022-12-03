from unittest import TestCase
from game import create_user


class TestCreateUser(TestCase):
    def test_create_user_Patty(self):
        test_name = "Patty"
        test_sub_name = "Happy"
        expected = {'attack': 20,
                    'column': 0,
                    'exp': 0,
                    'hp': 100,
                    'level': 1,
                    'morale': 3,
                    'name': 'Patty',
                    'row': 0,
                    'sub_name': 'Happy',
                    'treasure': False,
                    'death': False,
                    'guesses': 3}
        self.assertEqual(expected, create_user(test_name, test_sub_name))

    def test_create_user_Tim(self):
        test_name = "Tim"
        test_sub_name = "Energized"
        expected = {'name': 'Tim', 'sub_name': 'Energized', 'row': 0, 'column': 0, 'level': 1, 'exp': 0, 'morale': 3,
                    'hp': 100, 'attack': 20, 'treasure': False, 'death': False, 'guesses': 3}
        self.assertEqual(expected, create_user(test_name, test_sub_name))

    def test_create_user_empty_strings(self):
        test_name = ""
        test_sub_name = ""
        expected = {'name': '', 'sub_name': '', 'row': 0, 'column': 0, 'level': 1, 'exp': 0, 'morale': 3,
                    'hp': 100, 'attack': 20, 'treasure': False, 'death': False, 'guesses': 3}
        self.assertEqual(expected, create_user(test_name, test_sub_name))
