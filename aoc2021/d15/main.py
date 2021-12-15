from helpers import *
from collections import defaultdict, Counter
from queue import PriorityQueue
import numpy as np

lines = load_file(15, test=0)
lines = [line.rstrip() for line in lines]

for i, line in enumerate(lines):
    lines[i] = [int(l) for l in list(line)]

lines = np.array(lines, dtype=np.int8)


def clean_grid(grid):
    while any(grid[grid > 9]):
        grid[grid > 9] -= 9


lines = np.concatenate([(lines + i) for i in range(5)], axis=0)
clean_grid(lines)
lines = np.concatenate([(lines + i) for i in range(5)], axis=1)
clean_grid(lines)

values = np.full(lines.shape, np.inf)
visited = set()


def neighbours(grid, x, y):
    result = []
    if x + 1 < grid.shape[0]:
        result.append((x+1, y))
    if y + 1 < grid.shape[1]:
        result.append((x, y+1))
    if x - 1 >= 0:
        result.append((x-1, y))
    if y - 1 >= 0:
        result.append((x, y-1))
    return result


start = (0, 0)
pq = PriorityQueue()
pq.put((0, start))
values[start] = 0

while not pq.empty():
    dist, current = pq.get()
    visited.add(current)

    for neighbour in neighbours(lines, *current):
        distance = lines[neighbour]
        if neighbour not in visited:
            old_cost = values[neighbour]
            new_cost = values[current] + distance
            if new_cost < old_cost:
                pq.put((new_cost, neighbour))
                values[neighbour] = new_cost

print(values[-1, -1])
