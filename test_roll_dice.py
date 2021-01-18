from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_dice


class Test(TestCase):

    @patch('random.randint', return_value=5)
    def test_roll_dice_one_die(self, mock_input):
        actual = roll_dice(1)
        expected = [5]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[2, 6])
    def test_roll_dice_two_dice(self, mock_input):
        actual = roll_dice(2)
        expected = [2, 6]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[1, 5, 6, 3, 1])
    def test_roll_dice_five_dice(self, mock_input):
        actual = roll_dice(5)
        expected = [1, 5, 6, 3, 1]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=[5, 5, 5, 5])
    def test_roll_dice_four_dice(self, mock_input):
        actual = roll_dice(4)
        expected = [5, 5, 5, 5]
        self.assertEqual(expected, actual)
