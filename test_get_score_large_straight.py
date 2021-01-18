from unittest import TestCase
from yahtzee import get_score_large_straight


class Test(TestCase):

    def test_get_score_three_consecutive_numbers(self):
        players_dice = [1, 1, 3, 4, 5]
        actual = get_score_large_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_four_consecutive_numbers(self):
        players_dice = [1, 6, 3, 4, 5]
        actual = get_score_large_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_five_consecutive_numbers(self):
        players_dice = [1, 2, 3, 4, 5]
        actual = get_score_large_straight(players_dice)
        expected = 40
        self.assertEqual(expected, actual)

    def test_get_score_three_same_numbers(self):
        players_dice = [1, 3, 3, 3, 5]
        actual = get_score_large_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_five_consecutive_numbers_random_order(self):
        players_dice = [5, 3, 2, 6, 4]
        actual = get_score_large_straight(players_dice)
        expected = 40
        self.assertEqual(expected, actual)

    def test_get_score_five_same_numbers(self):
        players_dice = [5, 5, 5, 5, 5]
        actual = get_score_large_straight(players_dice)
        expected = 0
        self.assertEqual(expected, actual)
