from unittest import TestCase
from yahtzee import get_score_full_house


class Test(TestCase):

    def test_get_score_full_house_no_pairs(self):
        players_dice = [1, 6, 3, 4, 5]
        actual = get_score_full_house(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_full_house_one_pair(self):
        players_dice = [1, 6, 6, 4, 5]
        actual = get_score_full_house(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_full_house_two_pairs(self):
        players_dice = [6, 6, 3, 5, 5]
        actual = get_score_full_house(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_full_house_three_same_one_pair(self):
        players_dice = [6, 6, 4, 4, 4]
        actual = get_score_full_house(players_dice)
        expected = 25
        self.assertEqual(expected, actual)

    def test_get_score_full_house_four_same(self):
        players_dice = [4, 6, 4, 4, 4]
        actual = get_score_full_house(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_full_house_five_same(self):
        players_dice = [4, 4, 4, 4, 4]
        actual = get_score_full_house(players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_full_house_three_same_one_pair_different_order(self):
        players_dice = [4, 6, 4, 6, 4]
        actual = get_score_full_house(players_dice)
        expected = 25
        self.assertEqual(expected, actual)
