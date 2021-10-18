import random


def get_adversary_play(game_choices):
    adversary_choice = ''
    for i in range(10):
        adversary_choice = random.sample(game_choices,1)[0]

    return  adversary_choice
