GAME_PROMPT = '        (0-2)-> '

def print_header():
    print('''\n
        JJJJJ  U   U  N   N  K   K  EEEEE  N   N  PPPP     OO
            J  U   U  NN  N  K  K   E      NN  N  P   P  O    O
            J  U   U  N N N  KKK    EEE    N N N  PPPP   O    O
        J   J  U   U  N  NN  K  K   E      N  NN  P      O    O
         JJJ    UUU   N   N  K   K  EEEEE  N   N  P        OO
            \n''')
    print("\n        Simple Jun Ken Po (Rock Paper Scissor) game.\n", \
            "        This is a terminal version of a 1 player game")
    print()


def print_choices():
    print('\n        ====================================')
    print('        Select your play:\n',\
            '        0 - Rock\n',\
            '        1 - Paper\n',\
            '        2 - Scissor\n')
    print('        - hit an empty input to quit or "quit" -')
    print('        ====================================\n')


def print_goodbye():
    print("        Thank´s for playing!\n        Until next time!")


def print_invalid_choice():
    print("        Invalid play, please choose beween 0, 1 or 2.\n")

def print_plays(player_play, adversary_play):
    print_player_play(player_play)
    print_adversary_play(adversary_play)

def print_player_play(player_play):
    print('        You choose %s'%(player_play))

def print_adversary_play(adversary_play):
    print('        You adversary choose %s \n'%(adversary_play))

def draw_game():
    print('        | It´s draw! |')


def loose_game():
    print('        .--. |       You Loose!      | .--.\n',\
           '       .--. | Better luky next time | .--.')


def win_game():
    print('        \\**/ | You won! Congrats | \\**/')
