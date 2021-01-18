"""
Henry Chu
A01212982
Final Exam: Yahtzee
"""
import doctest
import random
import re


def create_player() -> dict:
    """
    Asks the user for the player name.

    :return:        a dictionary of the player name and scoreboard
    """

    player_name = input('Please enter your name: ')
    while not player_name.strip():
        player_name = input('Please enter your name again: ')
    player = {'name': player_name,
              'score': {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, 'sixes': -1,
                        'three-of-a-kind': -1, 'four-of-a-kind': -1, 'full-house': -1,
                        'small straight': -1, 'large straight': -1, 'chance': -1, 'yahtzee': -1}}

    return player


def roll_dice(number_of_dice: int) -> list:
    """
    Rolls a number of dice.

    :param number_of_dice:      the number of dice
    :precondition:              number_of_dice is an integer
    :postcondition:             the dice gives a random number between 1 - 6
    :return:                    list of  integer numbers 1-6
    """

    dice = [random.randint(1, 6) for number in range(1, number_of_dice + 1)]
    return dice


def re_roll_dice(list_of_dice, reroll_choices):
    """
    Rerolls the dice that the player chooses with the indices.

    :param list_of_dice:        the players list of dice values
    :param reroll_choices:      list of dice player chose to reroll(dice indices) as a string
    :precondition:              both parameters are lists
    :postcondition:             rerolls the dice of the players choice
    """
    reroll_choices = reroll_choices.replace(" ", "")
    dice_rerolled = roll_dice(len(reroll_choices))
    for number in reroll_choices:
            list_of_dice[int(number) - 1] = dice_rerolled.pop()


def player_turn(scoreboard: dict):
    """
    Determines what happens in the player's turn.

    Rolls the dice-hand and asks if user wants to reroll.

    :param scoreboard:  the player's scoreboard
    :precondition:      the player must be a dictionary
    :postcondition:     determines what the player does in the turn
    :return:            the players dice hand
    """

    dice_hand = roll_dice(5)
    print(*dice_hand, sep=' ')
    players_choice = input('Would you like to (1)reroll or (2) score? Enter the number: ').lower()

    while players_choice != '1' and players_choice != '2':
        players_choice = input("Sorry, invalid response, please choose again: ")

    if players_choice == '1':
        reroll_phase(dice_hand, scoreboard)
        return dice_hand
    else:
        for number, key in enumerate(scoreboard.keys(), 1):
            print(number, key)
        return dice_hand


def reroll_phase(list_of_dice, scoreboard):
    """
    Determines what dice to reroll.

    :param list_of_dice:        the player's list of dice values
    :param scoreboard:          the player's scoreboard
    :precondition:              both parameters are lists
    :postcondition:             rerolls the dice one or two times
    :return:                    rerolled dice
    """

    reroll_times = 2
    players_choice = 'y'
    while reroll_times > 0 and players_choice == 'y':
        dice_to_reroll = input('Please choose the dice number(1-5), not the value: ')
        re_roll_dice(list_of_dice, dice_to_reroll)
        print(*list_of_dice, sep=' ')
        reroll_times -= 1
        if reroll_times > 0:
            players_choice = input('Would you like to reroll? (y or n): ').lower()

    for number, key in enumerate(scoreboard.keys(), 1):
        print(number, key)


def validate_options(scoreboard: dict, player_choice: int, is_yahtzee):
    """
    Check the option the player chose in main.

    :param scoreboard:          the players scoreboard
    :param player_choice:       option the player chose
    :param is_yahtzee:          dice hand is a yahtzee
    :precondition:              scoreboard_dictionary must be a dictionary
                                player_choice must be an integer
    :postcondition:             checks which option is available
    :return:                    true if its possible, false if not
    """

    for number, score_item in enumerate(scoreboard.items(), 1):
        if player_choice == number:
            if score_item[1] >= 0:
                if player_choice == 13 and score_item[1] > 0 and is_yahtzee:
                    # Allows user to choose yahtzee score if score is greater than 0
                    return True
                return False
    return True


def validate_dice_hand(option_chosen, list_of_dice, scoreboard, is_yahtzee) -> int:
    """
    Validates the players dice hand.

    Calculates the score.

    :param scoreboard:      player scoreboard
    :param is_yahtzee:      player hand is yahtzee or not
    :param option_chosen:   the option the player chose
    :param list_of_dice:    the players hand of dice
    :precondition:          the option must be an integer
                            the list_of_dice must be a list
    :postcondition:         validates the hand and calculates the score
    :return:                the score as an int
    """

    list_get_scores = [get_score_three_of_a_kind(list_of_dice), get_score_four_of_a_kind(list_of_dice),
                       get_score_full_house(list_of_dice), get_score_small_straight(list_of_dice),
                       get_score_large_straight(list_of_dice), get_score_total(list_of_dice),
                       get_yahtzee_score(is_yahtzee, scoreboard)]

    if option_chosen <= 6:
        return get_score_upper_section(option_chosen, list_of_dice)
    else:
        return list_get_scores[option_chosen - 7]


def update_score(scoreboard, score, option_chosen):
    """

    :param scoreboard:      the players scoreboard
    :param score:           the score for the dice hand
    :param option_chosen:   the players choice of score
    :precondition:          scoreboard is a dictionary
                            list_of_dice is a list
    :postcondition:         updates the players scoreboard
    """

    scoreboard_keys = list(scoreboard.keys())
    choice = scoreboard_keys[option_chosen - 1]
    scoreboard[choice] = score


def FULL_HOUSE_SCORE():
    """
    Returns a full-house score constant.
    """

    return 25


def SMALL_STRAIGHT_SCORE():
    """
    Returns a small straight score constant.
    """

    return 30


def LARGE_STRAIGHT_SCORE():
    """
    Returns a large straight score constant.
    """

    return 40


def YAHTZEE_SCORE():
    """
    Returns a yahtzee score constant.
    """

    return 50


def YAHTZEE_BONUS_SCORE():
    """
    Returns a bonus yahtzee score constant.
    """

    return 100


def get_score_upper_section(option_chosen, list_of_dice):
    """
    Calculates the score in the upper section.

    Takes options 1 - 6.

    :param option_chosen:   the option the player chose
    :param list_of_dice:    the players hand of dice
    :precondition:          the option must be an integer
                            the list_of_dice must be a list
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_upper_section(1, [1, 1, 2, 2, 5])
    2
    >>> get_score_upper_section(1, [3, 4, 2, 2, 5])
    0
    >>> get_score_upper_section(6, [5, 6, 6, 2, 5])
    12
    """

    score = list_of_dice.count(option_chosen) * option_chosen
    return score


def get_score_three_of_a_kind(list_of_dice):
    """
    Calculates the score for three of a kind.

    :param list_of_dice:    the players hand of dice
    :precondition:          the list_of_dice must be a list
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_three_of_a_kind([1, 1, 2, 2, 5])
    0
    >>> get_score_three_of_a_kind([1, 2, 2, 2, 5])
    12
    >>> get_score_three_of_a_kind([1, 2, 2, 2, 2])
    9
    """

    string_list_of_dice = [str(number) for number in list_of_dice]
    string_list_of_dice = ''.join(string_list_of_dice)

    score = 0
    if re.compile(r'(.)\1{2}').search(string_list_of_dice):
        score = get_score_total(list_of_dice)
    return score


def get_score_four_of_a_kind(list_of_dice):
    """
    Calculates the score for four of a kind.

    :param list_of_dice:    the players hand of dice
    :precondition:          the list_of_dice must be a list
    :postcondition:         calculates the score
    :return:                the score for the dic hand

    >>> get_score_four_of_a_kind([1, 1, 2, 2, 5])
    0
    >>> get_score_four_of_a_kind([1, 2, 2, 2, 5])
    0
    >>> get_score_four_of_a_kind([1, 5, 5, 5, 5])
    21
    """

    string_list_of_dice = [str(number) for number in list_of_dice]
    string_dice = ''.join(string_list_of_dice)

    score = 0
    if re.compile(r'(.)\1{3}').search(string_dice):
        score = get_score_total(list_of_dice)
    return score


def get_score_total(list_of_dice):
    """
    Calculates the total of dice-hand.

    :param list_of_dice:    the players hand of dice
    :precondition:          the list_of_dice must be a list
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_total([1, 1, 2, 2, 5])
    11
    >>> get_score_total([1, 2, 2, 2, 5])
    12
    """

    score = 0
    for number in list_of_dice:
        score += number
    return score


def get_score_full_house(list_of_dice):
    """
    Calculates the score for full house.

    :param list_of_dice:    the players hand of dice
    :precondition:          the option must be an integer
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_full_house([1, 1, 2, 2, 5])
    0
    >>> get_score_full_house([1, 1, 2, 2, 1])
    25
    >>> get_score_full_house([1, 3, 2, 4, 5])
    0
    >>> get_score_full_house([1, 5, 1, 5, 5])
    25
    >>> get_score_full_house([5, 6, 2, 2, 5])
    0
    """

    sorted_list_of_dice = sorted(list_of_dice)
    string_list_of_dice = [str(number) for number in sorted_list_of_dice]
    string_dice = ''.join(string_list_of_dice)

    if (re.compile(r'(.)\1(.)\2{2}').search(string_dice)
            or re.compile(r'(.)\1{2}(.)\2').search(string_dice)):
        return FULL_HOUSE_SCORE()
    return 0


def get_score_small_straight(list_of_dice):
    """
    Calculates the score small straights.

    :param list_of_dice:    the players hand of dice
    :precondition:          the option must be an integer
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_small_straight([1, 1, 2, 2, 5])
    0
    >>> get_score_small_straight([1, 1, 2, 2, 1])
    0
    >>> get_score_small_straight([1, 3, 2, 4, 5])
    30
    >>> get_score_small_straight([1, 3, 2, 4, 6])
    30
    >>> get_score_small_straight([5, 6, 2, 2, 5])
    0
    """
    no_duplicate_list_of_dice = list(dict.fromkeys(list_of_dice))
    sorted_list_of_dice = sorted(no_duplicate_list_of_dice)
    string_list_of_dice = [str(number) for number in sorted_list_of_dice]
    string_dice = ''.join(string_list_of_dice)

    if re.compile(r'1234').search(string_dice) or re.compile(r'2345').search(string_dice) \
            or re.compile(r'3456').search(string_dice):
        return SMALL_STRAIGHT_SCORE()
    return 0


def get_score_large_straight(list_of_dice):
    """
    Calculates the score for large straights.

    :param list_of_dice:    the players hand of dice
    :precondition:          the option must be an integer
    :postcondition:         calculates the score
    :return:                the score for the dice hand

    >>> get_score_large_straight([1, 1, 2, 2, 5])
    0
    >>> get_score_large_straight([1, 1, 2, 2, 1])
    0
    >>> get_score_large_straight([1, 3, 2, 5, 4])
    40
    >>> get_score_large_straight([1, 3, 2, 4, 6])
    0
    >>> get_score_large_straight([1, 2, 3, 4, 5])
    40
    """

    sorted_list_of_dice = sorted(list_of_dice)
    string_list_of_dice = [str(number) for number in sorted_list_of_dice]
    string_dice = ''.join(string_list_of_dice)

    if re.compile(r'12345').search(string_dice) or (re.compile(r'23456').search(string_dice)):
        return LARGE_STRAIGHT_SCORE()
    return 0


def get_yahtzee_score(is_yahtzee, player_scoreboard):
    """
    Calculates the score for a yahtzee.

    If player already has a yahtzee score of 50, additional yahtzees are 100 points.

    :param is_yahtzee:          the players hand is yahtzee or not
    :param player_scoreboard:   the players scorebaord
    :precondition:              the option must be an integer
                                the list_of_dice must be a list
    :postcondition:             calculates the score
    :return:                    the score for the dice hand

    >>> get_yahtzee_score(False, {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, \
                         'fives': -1, 'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1, 'full-house': -1, \
                         'small straight': -1, 'large straight': -1, 'chance': -1, 'yahtzee': -1})
    0
    >>> get_yahtzee_score(True, {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, \
                         'fives': -1, 'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1, 'full-house': -1, \
                         'small straight': -1, 'large straight': -1, 'chance': -1, 'yahtzee': -1})
    50
    >>> get_yahtzee_score(True, {'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, \
                         'fives': -1, 'sixes': -1, 'three-of-a-kind': -1, 'four-of-a-kind': -1, 'full-house': -1, \
                         'small straight': -1, 'large straight': -1, 'chance': -1, 'yahtzee': 50})
    100
    """

    if is_yahtzee:
        if player_scoreboard['yahtzee'] > 0:
            return YAHTZEE_BONUS_SCORE()
        else:
            return YAHTZEE_SCORE()
    return 0


def check_yahtzee(list_of_dice):
    """
    Checks if the dice hand is yahtzee or not

    :param list_of_dice:    players dice hand
    :precondition:          list_of_dice is a list
    :postcondition:         validates hand is yahtzee
    :return:                True if yahtzee
                            False if not

    >>> check_yahtzee([1, 2, 3, 4, 5])
    False
    >>> check_yahtzee([3, 5, 3, 4, 5])
    False
    >>> check_yahtzee([5, 5, 5, 5, 5])
    YAHTZEEEEEEEEEEEEEEEEEEEEEEEE!!!
    True
    """
    string_list_of_dice = [str(number) for number in list_of_dice]
    string_dice = ''.join(string_list_of_dice)
    if re.compile(r'(.)\1{4}').search(string_dice):
        print("YAHTZEEEEEEEEEEEEEEEEEEEEEEEE!!!")
        return True
    return False


def validate_complete_board(players_scoreboard):
    """
    Checks if the scoreboard is complete.

    :param players_scoreboard:  the players scoreboard
    :precondition:              the scoreboard must be a dictionary
    :postcondition:             checks if the scoreboard is complete
    :return:                    True if complete, False if not

    >>> validate_complete_board({'ones': -1, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, \
                               'sixes': -1, 'three of a kind': -1, 'four of a kind': -1, \
                               'full house': -1, 'small straight': -1, 'large straight': -1, \
                               'chance': -1, 'yahtzee': -1})
    False

    >>> validate_complete_board({'ones': 3, 'twos': -1, 'threes': -1, 'fours': -1, 'fives': -1, \
                               'sixes': -1, 'three of a kind': 15, 'four of a kind': -1, \
                               'full house': 25, 'small straight': -1, 'large straight': -1, \
                               'chance': -1, 'yahtzee': 50})
    False

    >>> validate_complete_board({'ones': 3, 'twos': 2, 'threes': 9, 'fours': 8, 'fives': 15, \
                               'sixes': 18, 'three of a kind': 16, 'four of a kind': 20, \
                               'full house': 25, 'small straight': 30, 'large straight': 40, \
                               'chance': 20, 'yahtzee': 50})
    True
    """

    for value in players_scoreboard.values():
        if value == -1:
            return False
    return True


def get_player_score(scoreboard):
    """
    Calculates the player's total score

    :param scoreboard:  players scoreboard
    :precondition:      scoreboard is a dictionary
    :postcondition:     adds the scores together
    :return:            players score

    >>> get_player_score({'ones': 3, 'twos': 2, 'threes': 9, 'fours': 8, 'fives': 15, \
                         'sixes': 18, 'three of a kind': 16, 'four of a kind': 20, \
                         'full house': 25, 'small straight': 30, 'large straight': 40, \
                         'chance': 20, 'yahtzee': 50})
    256
    >>> get_player_score({'ones': 0, 'twos': 2, 'threes': 9, 'fours': 8, 'fives': 15, \
                         'sixes': 18, 'three of a kind': 16, 'four of a kind': 20, \
                         'full house': 25, 'small straight': 30, 'large straight': 40, \
                         'chance': 0, 'yahtzee': 0})
    183
    >>> get_player_score({'ones': 0, 'twos': 0, 'threes': 0, 'fours': 0, 'fives': 0, \
                        'sixes': 0, 'three of a kind': 0, 'four of a kind': 0, 'full house': 0, \
                        'small straight': 0, 'large straight': 0, 'chance': 5, 'yahtzee': 0})
    5
    """

    player_total_score = 0
    upper_section_score = 0
    for number, value in enumerate(scoreboard.values(), 1):
        if number <= 6:
            upper_section_score += value
        player_total_score += value
    if upper_section_score >= 63:
        player_total_score += 35
    return player_total_score


def main():
    """
    Drives the program.
    """
    print('Hello players, to this amazing game of Yahtzee!')
    print('First player')
    player_one = create_player()
    print('Second Player')
    player_two = create_player()
    while not validate_complete_board(player_one['score']) and \
            not validate_complete_board(player_two['score']):
        if not validate_complete_board(player_one['score']):
            print("Player one's turn")
            dice_hand = player_turn(player_one['score'])
            dice_hand_is_yahtzee = check_yahtzee(dice_hand)
            score_option = input('Please enter the number of your choice: ')
            while not validate_options(player_one['score'], int(score_option), dice_hand_is_yahtzee):
                score_option = input('Please enter a different choice: ')
            score = validate_dice_hand(int(score_option), dice_hand, player_one['score'], dice_hand_is_yahtzee)
            update_score(player_one['score'], score, int(score_option))
            print(player_one)
        if not validate_complete_board(player_two['score']):
            print("Player two's turn")
            dice_hand = player_turn(player_two['score'])
            dice_hand_is_yahtzee = check_yahtzee(dice_hand)
            score_option = input('Please enter the number of your choice: ')
            while not validate_options(player_two['score'], int(score_option), dice_hand_is_yahtzee):
                score_option = input('Please enter a different choice: ')
            score = validate_dice_hand(int(score_option), dice_hand, player_two['score'], dice_hand_is_yahtzee)
            update_score(player_two['score'], score, int(score_option))
            print(player_two)

    player_one_total_score = get_player_score(player_one['score'])
    player_two_total_score = get_player_score(player_two['score'])

    if player_one_total_score > player_two_total_score:
        name = player_one['name']
        print('Congratulations,', name, '! You have won this round!')
    elif player_two_total_score > player_one_total_score:
        name = player_two['name']
        print('Congratulations,', name, '! You have won this round!')
    else:
        print('OMG its a TIE!')

    doctest.testmod()


if __name__ == '__main__':
    main()

