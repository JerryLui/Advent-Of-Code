from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(11)
lines = [line.rstrip() for line in lines]

# lines = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526"""
# lines = lines.splitlines()
tmp = []
for row in lines:
    tmp.append([int(i) for i in list(row)])
lines = np.array(tmp, dtype=np.int8)


explosions = 0
new_explosions = 0


def step(m):
    global new_explosions
    blow = set()
    new_explosions = 0
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            m[i, j] += 1
            if m[i, j] > 9:
                blow.add((i, j))

    explode(m, blow)
    if new_explosions == m.size:
        print(m)
        raise Exception('Done')


def explode(m, blow):
    global explosions
    global new_explosions
    secondary = []
    for pt in blow:
        explosions += 1
        new_explosions += 1
        m[pt] = 0
        secondary += list(set(neighbours(m, pt)) - blow)

    new = set()
    for pt in secondary:
        if m[pt]:
            m[pt] += 1
            if m[pt] > 9:
                new.add(pt)
    if new:
        explode(m, new)


def neighbours(m, pt):
    x, y = pt
    n = {(x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y)}
    if x == 0:
        n -= {(x-1, y-1), (x-1, y), (x-1, y+1)}
    elif x == m.shape[1]-1:
        n -= {(x + 1, y + 1), (x + 1, y), (x + 1, y - 1)}
    if y == 0:
        n -= {(x+1, y-1), (x, y-1), (x-1, y-1)}
    elif y == m.shape[0]-1:
        n -= {(x - 1, y + 1), (x, y + 1), (x + 1, y + 1), }
    return n


for i in range(10000):
    print(i)
    step(lines)
print(explosions)



