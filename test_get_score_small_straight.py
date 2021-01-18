from unittest import TestCase
from yahtzee import get_score_small_straight


class Test(TestCase):

    def test_get_score_three_consecutive_numbers(self):
        players_dice = [1, 1, 3, 4, 5]
        actual = get_score_small_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_four_consecutive_numbers(self):
        players_dice = [1, 6, 3, 4, 5]
        actual = get_score_small_straight(players_dice)
        expected = 30
        self.assertEqual(expected, actual)

    def test_get_score_five_consecutive_numbers(self):
        players_dice = [1, 2, 3, 4, 5]
        actual = get_score_small_straight(players_dice)
        expected = 30
        self.assertEqual(expected, actual)

    def test_get_score_three_same_numbers(self):
        players_dice = [1, 1, 1, 4, 5]
        actual = get_score_small_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_five_consecutive_numbers(self):
        players_dice = [1, 1, 1, 1, 1]
        actual = get_score_small_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_three_same_one_pair(self):
        players_dice = [1, 1, 3, 3, 3]
        actual = get_score_small_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)
