import random
from game import GAME_CHOICES


def get_adversary_play():
    adversary_choice = ''
    for i in range(10):
        adversary_choice = random.sample(GAME_CHOICES,1)[0]

    return  adversary_choice
