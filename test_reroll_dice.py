from unittest import TestCase
from unittest.mock import patch
from yahtzee import re_roll_dice


class Test(TestCase):

    @patch('random.randint', return_value=[5])
    def test_re_roll_dice_one_die(self, mock_input):
        list_of_dice = [6, 4, 1, 2, 5]
        reroll_choices = "1"
        actual = re_roll_dice(list_of_dice, reroll_choices)
        expected = [5, 4, 1, 2, 5]
        self.assertListEqual(expected, actual)

    @patch('random.randint', return_value=[5, 2])
    def test_re_roll_dice_two_dice(self,mock_input):
        list_of_dice = [6, 4, 1, 2, 5]
        reroll_choices = "12"
        actual = re_roll_dice(list_of_dice, reroll_choices)
        expected = [5, 2, 1, 2, 5]
        self.assertListEqual(expected, actual)

    @patch('random.randint', return_value=[1, 1])
    def test_re_roll_dice_two_other_dice(self,mock_input):
        list_of_dice = [6, 4, 1, 2, 5]
        reroll_choices = "35"
        actual = re_roll_dice(list_of_dice, reroll_choices)
        expected = [5, 1, 1, 2, 1]
        self.assertListEqual(expected, actual)

    @patch('random.randint', return_value=[6, 4, 3, 6])
    def test_re_roll_dice_four_dice(self,mock_input):
        list_of_dice = [6, 4, 1, 2, 5]
        reroll_choices = "2345"
        actual = re_roll_dice(list_of_dice, reroll_choices)
        expected = [6, 6, 4, 3, 6]
        self.assertListEqual(expected, actual)

    @patch('random.randint', return_value=[5, 6, 4, 3, 5])
    def test_re_roll_dice_five_dice(self,mock_input):
        list_of_dice = [6, 4, 1, 2, 5]
        reroll_choices = "12345"
        actual = re_roll_dice(list_of_dice, reroll_choices)
        expected = [5, 6, 4, 3, 5]
        self.assertListEqual(expected, actual)
