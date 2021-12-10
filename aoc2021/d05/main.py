from helpers import *
import numpy as np

lines = load_file(5)
# lines = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()
lines = [l.rstrip().split(' -> ') for l in lines]

point_pairs = []
for line in lines:
    point_pairs.append([point.split(',') for point in line])

array = np.zeros((1000, 1000), dtype=np.int8)
for point_pair in point_pairs:
    x0 = int(point_pair[0][0])
    x1 = int(point_pair[1][0])
    y0 = int(point_pair[0][1])
    y1 = int(point_pair[1][1])
    if x0 == x1 or y0 == y1:
        for i in range(min(x0, x1), max(x0, x1)+1):
            for j in range(min(y0, y1), max(y0, y1)+1):
                array[i, j] += 1
    else:
        for i in range(max(x0, x1) - min(x0, x1) + 1):
            if x0 < x1 and y0 < y1:
                array[x0 + i, y0 + i] += 1
            elif x0 < x1 and y0 > y1:
                array[x0 + i, y0 - i] += 1
            elif x0 > x1 and y0 > y1:
                array[x0 - i, y0 - i] += 1
            else:
                array[x0 - i, y0 + i] += 1

dangers = 0
for row in array:
    for col in row:
        if col > 1:
            dangers += 1

print(dangers)
