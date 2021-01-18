from unittest import TestCase
from yahtzee import get_score_four_of_a_kind


class Test(TestCase):

    def test_get_score_four_kind_four_matches(self):
        players_dice = [2, 2, 2, 2, 5]
        actual = get_score_four_of_a_kind(players_dice)
        expected = 13
        self.assertEqual(expected, actual)

    def test_get_score_four_kind_three_matches(self):
        players_dice = [2, 2, 2, 1, 5]
        actual = get_score_four_of_a_kind(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_four_kind_5_matches(self):
        players_dice = [6, 6, 6, 6, 6]
        actual = get_score_four_of_a_kind(players_dice)
        expected = 30
        self.assertEqual(expected, actual)

    def test_get_score_four_kind_1_matches(self):
        players_dice = [6, 4, 1, 2, 5]
        actual = get_score_four_of_a_kind( players_dice)
        expected = 0
        self.assertEqual(expected, actual)

