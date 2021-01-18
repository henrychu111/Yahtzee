from unittest import TestCase
from yahtzee import get_score_three_of_a_kind


class Test(TestCase):

    def test_get_score_three_kind_no_matches(self):
        players_dice = [1, 6, 3, 4, 5]
        actual = get_score_three_of_a_kind(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_three_kind_1_match(self):
        players_dice = [2, 3, 4, 5, 5]
        actual = get_score_three_of_a_kind(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_three_kind_three_matches(self):
        players_dice = [2, 2, 2, 4, 5]
        actual = get_score_three_of_a_kind(players_dice)
        expected = 15
        self.assertEqual(expected, actual)

    def test_get_score_three_kind_four_matches(self):
        players_dice = [2, 2, 2, 2, 5]
        actual = get_score_three_of_a_kind(players_dice)
        expected = 13
        self.assertEqual(expected, actual)
