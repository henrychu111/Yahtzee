from unittest import TestCase
from unittest.mock import patch
from yahtzee import create_player


class Test(TestCase):

    @patch('builtins.input', side_effect=['', 'Henry'])
    def test_create_player_empty_input(self, mock_input):
        actual = create_player()
        expected = {'name': 'Henry', 'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                               'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
                                               'full-house': -1, 'small straight': -1, 'large straight': -1,
                                               'chance': -1, 'yahtzee': -1}}
        self.assertDictEqual(expected, actual)

    @patch('builtins.input', side_effect=['Henry'])
    def test_create_player_name(self, mock_input):
        actual = create_player()
        expected = {'name': 'Henry', 'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                               'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
                                               'full-house': -1, 'small straight': -1, 'large straight': -1,
                                               'chance': -1, 'yahtzee': -1}}
        self.assertDictEqual(expected, actual)

    @patch('builtins.input', side_effect=['jack'])
    def test_create_player_lowercase_name(self, mock_input):
        actual = create_player()
        expected = {'name': 'jack', 'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                              'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
                                              'full-house': -1, 'small straight': -1, 'large straight': -1,
                                              'chance': -1, 'yahtzee': -1}}
        self.assertDictEqual(expected, actual)

    @patch('builtins.input', side_effect=['Harvey_the_hard_worker'])
    def test_create_player_underscore_name(self, mock_input):
        actual = create_player()
        expected = {'name': 'Harvey_the_hard_worker',
                    'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                              'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
                              'full-house': -1, 'small straight': -1, 'large straight': -1,
                              'chance': -1, 'yahtzee': -1}}
        self.assertDictEqual(expected, actual)

    @patch('builtins.input', side_effect=['Jacomb896'])
    def test_create_player_numbered_name(self, mock_input):
        actual = create_player()
        expected = {'name': 'Jacomb896', 'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                                   'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1,
                                                   'full-house': -1, 'small straight': -1, 'large straight': -1,
                                                   'chance': -1, 'yahtzee': -1}}
        self.assertDictEqual(expected, actual)
