from unittest import TestCase
from yahtzee import validate_complete_board


class Test(TestCase):

    def test_validate_complete_board_all_empty(self):
        players_scoreboard = {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1,
                              'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                              'full house': -1, 'small straight': -1, 'large straight': -1,
                              'chance': -1, 'yahtzee': -1}
        actual = validate_complete_board(players_scoreboard)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_complete_board_one_filled(self):
        players_scoreboard = {'ones': -1, 'twos': 6, 'threes': -1, 'fours': -1, 'fives': -1,
                              'sixes': -1, 'three of a kind': -1, 'four of a kind': -1,
                              'full house': -1, 'small straight': -1, 'large straight': -1,
                              'chance': -1, 'yahtzee': -1}
        actual = validate_complete_board(players_scoreboard)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_complete_board_six_filled(self):
        players_scoreboard = {'ones': 4, 'twos': -1, 'threes': 3, 'fours': 12, 'fives': -1,
                              'sixes': 12, 'three of a kind': 15, 'four of a kind': -1,
                              'full house': -1, 'small straight': -1, 'large straight': -1,
                              'chance': -1, 'yahtzee': 50}
        actual = validate_complete_board(players_scoreboard)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_complete_board_twelve_filled(self):
        players_scoreboard = {'ones': 3, 'twos': 2, 'threes': 9, 'fours': 8, 'fives': 15,
                              'sixes': 18, 'three of a kind': 16, 'four of a kind': 20,
                              'full house': 25, 'small straight': 30, 'large straight': 40,
                              'chance': 20, 'yahtzee': -1}
        actual = validate_complete_board(players_scoreboard)
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_complete_board_all_filled(self):
        players_scoreboard = {'ones': 3, 'twos': 2, 'threes': 9, 'fours': 8, 'fives': 15,
                              'sixes': 18, 'three of a kind': 16, 'four of a kind': 20,
                              'full house': 25, 'small straight': 30, 'large straight': 40,
                              'chance': 20, 'yahtzee': 50}
        actual = validate_complete_board(players_scoreboard)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_complete_board_all_filled_3_zeroes(self):
        players_scoreboard = {'ones': 3, 'twos': 2, 'threes': 0, 'fours': 0, 'fives': 15,
                              'sixes': 18, 'three of a kind': 16, 'four of a kind': 20,
                              'full house': 0, 'small straight': 30, 'large straight': 40,
                              'chance': 20, 'yahtzee': 50}
        actual = validate_complete_board(players_scoreboard)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_complete_board_all_filled_lowest_score(self):
        players_scoreboard = {'ones': 0, 'twos': 0, 'threes': 0, 'fours': 0, 'fives': 0,
                              'sixes': 0, 'three of a kind': 0, 'four of a kind': 0, 'full house': 0,
                              'small straight': 0, 'large straight': 0, 'chance': 5, 'yahtzee': 0}
        actual = validate_complete_board(players_scoreboard)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_complete_board_all_filled_very_high_score(self):
        players_scoreboard = {'ones': 2, 'twos': 6, 'threes': 9, 'fours': 8, 'fives': 15,
                              'sixes': 18, 'three of a kind': 12, 'four of a kind': 26, 'full house': 25,
                              'small straight': 30, 'large straight': 40, 'chance': 10, 'yahtzee': 450}
        actual = validate_complete_board(players_scoreboard)
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_complete_board_all_filled_all_zeroes(self):
        """
        An impossible scoring board, but meets validation requirement.
        """
        players_scoreboard = {'ones': 0, 'twos': 0, 'threes': 0, 'fours': 0, 'fives': 0,
                              'sixes': 0, 'three of a kind': 0, 'four of a kind': 0, 'full house': 0,
                              'small straight': 0, 'large straight': 0, 'chance': 0, 'yahtzee': 0}
        actual = validate_complete_board(players_scoreboard)
        expected = True
        self.assertEqual(expected, actual)
