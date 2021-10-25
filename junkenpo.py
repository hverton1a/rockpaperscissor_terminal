#! python
from game.adversary import *
from game.game import *
from game.gui import *
from game.player import *


def main():

    print_header()

    while True:
        print_choices()

        player_choice = get_player_choice()

        if player_choice == None:
            print_invalid_choice()
            continue

        player_play = get_player_play(player_choice)

        adversary_play = get_adversary_play()

        print_plays(player_play,adversary_play)

        game_result(player_play,adversary_play)


if __name__ == '__main__':
    main()
