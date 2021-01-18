from unittest import TestCase
from yahtzee import yahtzee_score


class Test(TestCase):

    def test_get_score_yahtzee_zero_same(self):
        option_chosen = 13
        players_dice = [1, 2, 3, 4, 5]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_yahtzee_2_same(self):
        option_chosen = 13
        players_dice = [4, 2, 3, 4, 5]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_yahtzee_four_same(self):
        option_chosen = 13
        players_dice = [4, 4, 4, 4, 5]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_score_yahtzee_five_same(self):
        option_chosen = 13
        players_dice = [4, 4, 4, 4, 4]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 50
        self.assertEqual(expected, actual)

    def test_get_score_yahtzee_five_same(self):
        option_chosen = 13
        players_dice = [4, 4, 4, 4, 4]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 50
        self.assertEqual(expected, actual)

    def test_get_score_second_yahtzee_five_same(self):
        option_chosen = 13
        players_dice = [6, 6, 6, 6, 6]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 100
        self.assertEqual(expected, actual)

    def test_get_score_fifth_yahtzee_five_same(self):
        option_chosen = 13
        players_dice = [6, 6, 6, 6, 6]
        actual = yahtzee_score(option_chosen, players_dice)
        expected = 100
        self.assertEqual(expected, actual)
