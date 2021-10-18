import random



def main():
    print("simple Jun Ken Po (Rock Paper Scissor) game.\n\
            This is a terminal version of a 1 player game ")

    enum_choices = ['Rock','Paper','Scissor']
    weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

    while True:
        print()
        print('Select your play:\n 0 - Rock\n 1 - Paper\n 2 - Scissor\n')
        print('hit an empty input to quit or "quit"')
        try:
            player_play = input('(0-2)>')
            print()
            if (player_play == '' or player_play == None or player_play == 'quit'):
                break
            player_play = int(player_play)

            if ( (player_play > 2 or player_play < 0) and type(player_play) == int):
                print("Invalid play, please choose beween 0, 1 or 2.\n")
                continue

            player_play = enum_choices[int(player_play)]
            print('You choose ',player_play)
        except ValueError:
            print("Invalid play, please choose beween 0, 1 or 2.\n")
            continue

        for i in range(10):
            cpu_play = random.sample(enum_choices,1)[0]
        print('You adversary choose ',cpu_play,'\n')

        result=''

        if (player_play == cpu_play):
            result = 'It´s a draw!'
        elif (weakness[player_play] == cpu_play):
            result = 'You Loose! Better luky next time'
        else:
            result = "You won! Congrats"

        print(result)



if __name__ == '__main__':
    main()
