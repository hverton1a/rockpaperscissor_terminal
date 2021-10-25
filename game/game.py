import sys
from gui import *

GAME_CHOICES = ['Rock','Paper','Scissor']

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
