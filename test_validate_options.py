from unittest import TestCase
from yahtzee import validate_options


class Test(TestCase):

    def test_validate_option_1_empty(self):
        scoreboard_dictionary = {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': -1, 'large straight': -1,
                                 'chance': -1, 'yahtzee': -1}
        players_choice = 1
        is_yahtzee = False
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_option_13_empty(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': 0, 'yahtzee': -1}
        players_choice = 13
        is_yahtzee = False
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_option_1_has_value(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': 0, 'yahtzee': 150}
        players_choice = 1
        is_yahtzee = False
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_option_8_has_value(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': 0,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': 0, 'yahtzee': 150}
        players_choice = 8
        is_yahtzee = False
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_option_13_has_yahtzee(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': 0, 'yahtzee': 50}
        players_choice = 13
        is_yahtzee = True
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_option_10_zero_value(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': -1, 'yahtzee': 50}
        players_choice = 10
        is_yahtzee = False
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_option_13_has_2_yahtzees(self):
        scoreboard_dictionary = {'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                                 'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                                 'full house': -1, 'small straight': 0, 'large straight': -1,
                                 'chance': 0, 'yahtzee': 150}
        players_choice = 13
        is_yahtzee = True
        actual = validate_options(scoreboard_dictionary, players_choice, is_yahtzee)
        expected = True
        self.assertEqual(expected, actual)

