import random, sys

def print_header():
    print("simple Jun Ken Po (Rock Paper Scissor) game.\n\
            This is a terminal version of a 1 player game ")
    print()

def print_choices():
    print('Select your play:\n 0 - Rock\n 1 - Paper\n 2 - Scissor\n')
    print('hit an empty input to quit or "quit"')


def player_is_quiting(player_choice):
    if (player_choice == '' or player_choice == None or player_choice == 'quit'):
        sys.exit()


def player_choice_is_valid(player_choice):
    return ( ( player_choice < 0 or player_choice > 2)
                or type(player_choice) != int )

def get_adversary_choice(game_choices):
    adversary_choice = ''
    for i in range(10):
        adversary_choice = random.sample(game_choices,1)[0]

    return  adversary_choice


def main():
    game_choices = ['Rock','Paper','Scissor']
    weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

    print_header()
    while True:
        print_choices()
        try:
            input_player_choice = input('(0-2)>')
            print()
            player_is_quiting(input_player_choice)
            player_choice = int(input_player_choice)
            if player_choice_is_valid(player_choice):
                print("Invalid play, please choose beween 0, 1 or 2.\n")
                continue
            player_play = game_choices[player_choice]
        except ValueError:
            print("Invalid play, please choose beween 0, 1 or 2.\n")
            continue

        adversary_play = get_adversary_choice(game_choices)

        print('You choose ',player_play)
        print('You adversary choose ',adversary_play,'\n')

        result=''

        if (player_play == adversary_play):
            result = 'It´s a draw!'
        elif (weakness[player_play] == adversary_play):
            result = 'You Loose! Better luky next time'
        else:
            result = "You won! Congrats"

        print(result)



if __name__ == '__main__':
    main()
