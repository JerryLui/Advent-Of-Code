from helpers import *
from collections import defaultdict, Counter
import numpy as np
import re

lines = load_file(25, test=0)
lines = [line.rstrip() for line in lines]

mappings = {'.': 0, '>': 1, 'v': 2}
reverse_mappings = {v: k for k, v in mappings.items()}

grid = []
for line in lines:
    grid.append(list(map(lambda x: mappings[x], line)))
grid = np.array(grid, dtype=np.int8)


def translate_grid():
    translated = []
    for row in grid:
        tmp = []
        for col in row:
            tmp.append(reverse_mappings[col])
        translated.append(''.join(tmp))
    return translated


step = 0
while True:
    moved = False
    tmp = np.zeros(grid.shape, dtype=np.int8)
    for i in range(grid.shape[0] - 1, -1, -1):
        for j in range(grid.shape[1] - 1, -1, -1):
            n_pos = None
            if step % 2 and grid[i, j] == 2:
                n_pos = (0, j) if i == grid.shape[0] - 1 else (i + 1, j)
            elif not step % 2 and grid[i, j] == 1:
                n_pos = (i, 0) if j == grid.shape[1] - 1 else (i, j + 1)

            if n_pos and not grid[n_pos]:
                tmp[n_pos] = grid[i, j]
                moved = True
            elif grid[i, j]:
                tmp[i, j] = grid[i, j]

    grid = tmp
    step += 1
    # [print(r) for r in translate_grid()]
    if not moved and step % 2:
        break

print(step/2)
