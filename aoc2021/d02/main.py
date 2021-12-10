from helpers import *
import numpy as np
from collections import defaultdict, Counter

lines = load_file(2)
lines = [line.rstrip() for line in lines]

aim = 0
h = 0
d = 0

for line in lines:
    op = line.split()[0]
    if op == 'forward':
        h += int(line.split()[1])
        d += aim * int(line.split()[1])
    elif op == 'down':
        aim += int(line.split()[1])
    else:
        aim -= int(line.split()[1])

print(h*d)
