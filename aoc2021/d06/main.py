from helpers import *
import numpy as np
from collections import deque

lines = load_file(6)
# lines = ['3, 4, 3, 1, 2']
lines = [int(l) for l in lines[0].split(',')]

lines = np.array(lines)

population = [0] * 9
for fish in lines:
    population[fish] += 1
queue = deque(population)

for day in range(256):
    spawn = queue.popleft()
    queue[-2] += spawn
    queue.append(spawn)
print(sum(queue))



    # if day and not day % 6:
    #     new = lines
    # elif day and not day % 8:
    #     original += new

# print(original)

    # lines -= 1
    # negatives = lines == -1
    # lines[negatives] = 6
    #
    # new = np.array([8] * np.count_nonzero(negatives))
    # if any(new):
    #     lines = np.append(lines, new)
    # print(lines)

    # for line in lines:
    #     if line == 0:
    #         tmp.append(6)
    #         new.append(8)
    #     else:
    #         tmp.append(line-1)
    # lines = tmp + new

# print(len(lines))
# for day in range(18):
#     if day and day % 8:
#         new = [l - 8 + 8 for l in lines]

