from game import quit_game


def get_player_play(game_choices, player_choice):
    return game_choices[player_choice]


def get_player_choice():
    input_player_choice = input('(0-2)>')
    print()

    if player_is_quiting(input_player_choice):
        quit_game()

    return validate_player_choice(input_player_choice)


def validate_player_choice(input_player_choice):
    result = None
    try:
        result = int(input_player_choice)
        if  ( result < 0 or result > 2):
            result = None
    except ValueError:
        result = None

    return result


def player_is_quiting(player_choice):
    result = False
    if (player_choice == '' or player_choice == None or player_choice == 'quit'):
        result = True
    return result
