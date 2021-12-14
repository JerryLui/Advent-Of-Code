from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(14)
lines = [line.rstrip() for line in lines]

# lines = """NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".splitlines()
start = lines[0]
operations = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in lines[2:]}

# P1
# for i in range(10):
#     tmp = ''
#     for pos in range(len(start) - 1):
#         pair = start[pos:pos+2]
#         tmp += pair[0] + operations[pair]
#     tmp += pair[1]
#     start = tmp
#
#     print(i)

# P2
char_counter = Counter()
pair_counter = Counter()
for pos in range(len(start) - 1):
    pair = start[pos:pos + 2]
    pair_counter.update({pair: 1})

last_char = start[-1]
for i in range(40):
    tmp = Counter()
    for pair, repeat in pair_counter.items():
        new_char = operations[pair]
        tmp.update({pair[0] + new_char: repeat})
        tmp.update({new_char + pair[1]: repeat})

    pair_counter = tmp
    print(i)


char_counter.update(last_char)
for k, r in pair_counter.items():
    char_counter.update({k[0]: r})

print(char_counter)
print(char_counter.most_common()[0][1]-char_counter.most_common()[-1][1])