from unittest import TestCase
from yahtzee import get_score_total


class Test(TestCase):

    def test_get_score_three_consecutive_numbers(self):
        players_dice = [1, 1, 3, 4, 5]
        actual = get_score_total(players_dice)
        expected = 14
        self.assertEqual(expected, actual)

    def test_get_score_five_same_numbers(self):
        players_dice = [1, 1, 1, 1, 1]
        actual = get_score_total(players_dice)
        expected = 5
        self.assertEqual(expected, actual)

    def test_get_score_five_different_numbers(self):
        players_dice = [6, 1, 3, 4, 5]
        actual = get_score_total(players_dice)
        expected = 19
        self.assertEqual(expected, actual)

    def test_get_score_three_same_one_pair(self):
        players_dice = [6, 6, 3, 3, 3]
        actual = get_score_total(players_dice)
        expected = 21
        self.assertEqual(expected, actual)
