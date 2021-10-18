import sys
from gui import *


def get_game_result(player_play,adversary_play):
    weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

    if (player_play == adversary_play):
        result = '| It´s a draw! |'
    elif (weakness[player_play] == adversary_play):
        result = '.--. |       You Loose!      | .--.\n.--. | Better luky next time | .--.'
    else:
        result = '\**/ | You won! Congrats | \**/'

    return result


def game_result(player_play, adversary_play):
        weakness = {'Rock':'Paper','Paper':'Scissor','Scissor':'Rock'}

        if (player_play == adversary_play):
            draw_game()
        elif (weakness[player_play] == adversary_play):
            loose_game()
        else:
            win_game()


def quit_game():
    print_goodbye()
    sys.exit(0)
