import random

def print_header():
    print("simple Jun Ken Po (Rock Paper Scissor) game.\n\
            This is a terminal version of a 1 player game ")
    print()
    print('Select your play:\n 0 - Rock\n 1 - Paper\n 2 - Scissor\n')
    print('hit an empty input to quit or "quit"')

def player_is_quiting(player_choice):

def get_player_choice():
    try:
        player_choice = input('(0-2)>')
        print()
        player_is_quiting(player_choice)
        player_choice = int(player_choice)

        if ( (player_choice > 2 or player_choice < 0) and type(player_choice) != int):
            print("Invalid play, please choose beween 0, 1 or 2.\n")
            continue

        player_choice = enum_choices[int(player_choice)]
        print('You choose ',player_choice)
    except ValueError:
        print("Invalid play, please choose beween 0, 1 or 2.\n")
        continue

    return player_choice


def main():


    enum_choices = ['Rock','Paper','Scissor']
    weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

    while True:
        print_header()
        player_choice = get_player_choice()


        for i in range(10):
            adversary_choice = random.sample(enum_choices,1)[0]
        print('You adversary choose ',adversary_choice,'\n')

        result=''

        if (player_choice == adversary_choice):
            result = 'It´s a draw!'
        elif (weakness[player_choice] == adversary_choice):
            result = 'You Loose! Better luky next time'
        else:
            result = "You won! Congrats"

        print(result)



if __name__ == '__main__':
    main()
