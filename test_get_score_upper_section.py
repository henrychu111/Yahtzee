from unittest import TestCase
from yahtzee import get_score_upper_section


class Test(TestCase):

    def test_get_score_upper_section_ones_score_one(self):
        option_chosen = 1
        players_dice = [1, 2, 3, 4, 5]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 1
        self.assertEqual(expected, actual)

    def test_get_score_upper_section_ones_score_zero(self):
        option_chosen = 1
        players_dice = [6, 2, 3, 4, 5]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_upper_section_ones_score_five(self):
        option_chosen = 1
        players_dice = [1, 1, 1, 1, 1]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_score_upper_section_sixes_score_eighteen(self):
        option_chosen = 6
        players_dice = [6, 6, 3, 6, 5]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 18
        self.assertEqual(expected, actual)

    def test_get_score_upper_section_threes_score_six(self):
        option_chosen = 3
        players_dice = [1, 2, 3, 3, 5]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 6
        self.assertEqual(expected, actual)

    def test_get_score_upper_section_fours_score_sixteen(self):
        option_chosen = 4
        players_dice = [4, 2, 4, 4, 4]
        actual = get_score_upper_section(option_chosen, players_dice)
        expected = 16
        self.assertEqual(expected, actual)

