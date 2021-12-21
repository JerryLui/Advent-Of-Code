from helpers import *
from collections import Counter, defaultdict
import time

lines = load_file(21, test=0)
lines = [int(line.rstrip()[-1]) for line in lines]


def get_new_pos(s):
    return s % 10 if s % 10 else 10


dice_distr = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
p1_master_dict = defaultdict(Counter)
p2_master_dict = defaultdict(Counter)
p1_master_dict[lines[0]][0] = 1
p2_master_dict[lines[1]][0] = 1         # {'pos': {'scores': n}}

player = 0
winners = [0, 0]
start = time.process_time()
while True:
    current_player = player % 2
    if current_player == 0:
        current_pos_dict = p1_master_dict
    else:
        current_pos_dict = p2_master_dict

    new_pos_dict = defaultdict(Counter)
    for steps, mult in dice_distr.items():
        for pos, scores in current_pos_dict.items():
            if any(scores.values()):
                new_pos = get_new_pos(pos + steps)
                for score, count in scores.items():
                    new_score = score + new_pos
                    if new_score >= 21:
                        # 1 Hour debugging this, forgot about other realities :')
                        if current_player == 0:
                            other_realities = p2_master_dict
                        else:
                            other_realities = p1_master_dict
                        total_realities = sum(sum(counter.values()) for counter in other_realities.values())
                        winners[current_player] += count * mult * total_realities
                    else:
                        new_pos_dict[new_pos].update({new_score: count * mult})

    if current_player == 0:
        p1_master_dict = new_pos_dict.copy()
    else:
        p2_master_dict = new_pos_dict.copy()

    player += 1
    if not sum(sum(counter.values()) for counter in p1_master_dict.values()):
        break

stop = time.process_time()
print(stop-start)
print(winners)
