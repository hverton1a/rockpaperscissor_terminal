import random, sys

def print_header():
    print("Simple Jun Ken Po (Rock Paper Scissor) game.\n", \
            "This is a terminal version of a 1 player game")
    print()

def print_choices():
    print('\n====================================')
    print('Select your play:\n 0 - Rock\n 1 - Paper\n 2 - Scissor\n')
    print('hit an empty input to quit or "quit"')
    print('====================================\n')


def get_player_choice():
    input_player_choice = input('(0-2)>')
    print()

    player_is_quiting(input_player_choice)

    return validate_player_choice(input_player_choice)


def player_is_quiting(player_choice):
    if (player_choice == '' or player_choice == None or player_choice == 'quit'):
        sys.exit()


def validate_player_choice(input_player_choice):
    result = None
    try:
        result = int(input_player_choice)
        if  ( result < 0 or result > 2):
            result = None
    except ValueError:
        result = None

    return result


def get_adversary_choice(game_choices):
    adversary_choice = ''
    for i in range(10):
        adversary_choice = random.sample(game_choices,1)[0]

    return  adversary_choice


def get_game_result(player_play,adversary_play):
    weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

    if (player_play == adversary_play):
        result = '| It´s a draw! |'
    elif (weakness[player_play] == adversary_play):
        result = '.--. |       You Loose!      | .--.\n.--. | Better luky next time | .--.'
    else:
        result = '\**/ | You won! Congrats | \**/'

    return result


def main():

    print_header()

    while True:
        print_choices()

        player_choice = get_player_choice()

        if player_choice == None:
            print("Invalid play, please choose beween 0, 1 or 2.\n")
            continue

        game_choices = ['Rock','Paper','Scissor']

        player_play = game_choices[player_choice]

        adversary_play = get_adversary_choice(game_choices)

        print('You choose ',player_play)
        print('You adversary choose ',adversary_play,'\n')

        result = get_game_result(player_play,adversary_play)

        print(result)



if __name__ == '__main__':
    main()
