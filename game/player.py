from game import quit_game, GAME_CHOICES
from gui import GAME_PROMPT


def get_player_play(player_choice):
    return GAME_CHOICES[player_choice]


def get_player_choice():
    input_player_choice = input(GAME_PROMPT)
    input_player_choice = input_player_choice.lower().strip()
    print()

    result = validate_player_choice(input_player_choice)

    if player_is_quiting(result):
        quit_game()

    return result


def validate_player_choice(input_player_choice):
    result = None
    try:
        result = int(input_player_choice)
        if  ( result < 0 or result > 2):
            result = None
    except ValueError:
        if input_player_choice == '' or input_player_choice == 'quit':
            result = input_player_choice
        else:
            result = None

    return result


def player_is_quiting(player_choice):
    result = False
    if (player_choice == '' or player_choice == 'quit'):
        result = True
    return result
