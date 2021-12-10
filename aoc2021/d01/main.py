from helpers import *
import numpy as np
from collections import defaultdict, Counter

lines = load_file(1)
lines = [int(line.rstrip()) for line in lines]
# lines = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263"""
# lines = [int(l) for l in lines.splitlines()]


prev = np.inf
score = 0
# for i, line in enumerate(lines):
#     if line > prev:
#         score += 1
#     prev = line

for i in range(len(lines)-2):
    window = lines[i] + lines[i + 1] + lines[i + 2]
    if window > prev:
        score += 1
    prev = window

print(score)





