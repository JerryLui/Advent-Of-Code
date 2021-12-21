from helpers import *
from collections import Counter
import numpy as np

lines = load_file(21, test=0)
lines = [int(line.rstrip()[-1]) for line in lines]

pos = {0: lines[0], 1: lines[1]}
score = {0: 0, 1: 0}


def get_score(s):
    return s % 10 if s % 10 else 10


dice = 1
player = 0
while True:
    steps = 3 * dice + 3

    current_player = player % 2
    current_score = get_score(pos[current_player] + steps)
    print(current_score)
    score[current_player] += current_score
    pos[current_player] = current_score

    player += 1
    dice += 3

    if score[current_player] >= 1000:
        print(f'{score=}')
        break

print((dice - 1) * min(score.values()))