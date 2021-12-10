from helpers import *
import numpy as np
from collections import defaultdict, Counter
from dataclasses import dataclass
from itertools import chain

lines = load_file(9)
lines = [list(line.strip()) for line in lines]
# lines = """2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678"""
# lines = [list(line.strip()) for line in lines.splitlines()]


def is_low(m, x, y, rec=False, visited=None):
    check_idx = []
    visited = visited if visited else []
    if x == 0:
        if y == 0:
            check_idx.append((x + 1, y + 1))
        elif y == lines.shape[1] - 1:
            check_idx.append((x + 1, y - 1))
    elif x == lines.shape[0] - 1:
        if y == 0:
            check_idx.append((x - 1, y + 1))
        elif y == lines.shape[1] - 1:
            check_idx.append((x - 1, y - 1))

    if x + 1 < lines.shape[0]:
        check_idx.append((x + 1, y))
    if x - 1 >= 0:
        check_idx.append((x - 1, y))
    if y + 1 < lines.shape[1]:
        check_idx.append((x, y + 1))
    if y - 1 >= 0:
        check_idx.append((x, y - 1))

    if not rec:
        if all([m[x, y] < m[pos] for pos in check_idx]):
            visited.append((x, y))
            rec = True
        else:
            return 0

    if rec:
        for pos in check_idx:
            if m[pos] != 9 and m[x, y] < m[pos]:
                visited.append((pos[0], pos[1]))
                is_low(m, pos[0], pos[1], True, visited=visited)
    return visited


results = []
lines = np.array(lines, dtype=np.int8)
for i in range(lines.shape[0]):
    for j in range(lines.shape[1]):
        result = is_low(lines, i, j)
        if result:
            results.append(len(set(result)))

results.sort()
print(results[-3:])
