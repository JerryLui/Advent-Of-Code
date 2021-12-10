from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(13)
lines = [line.rstrip() for line in lines]

# lines = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5""".splitlines()

data = [(int(l.split(',')[0]), int(l.split(',')[1])) for l in lines if not l.startswith('fold') and l]
fold = [l.split()[-1] for l in lines if l.startswith('fold')]

# max_x = max([x for x, y in data])     # REEEEEEEE
# max_y = max([y for x, y in data])

matrix = np.zeros((895, 1311), dtype=np.int8)
for x, y in data:
    matrix[y, x] = 1


def fold_matrix(m, s, n):
    n = int(n)
    if s == 'x':
        p1 = m[:, :n]
        p2 = m[:, n+1:]
        return p1 + np.fliplr(p2)
    else:
        p1 = m[:n, :]
        p2 = m[n+1:, :]
        return p1 + np.flipud(p2)


# f = fold[0]
# matrix = fold_matrix(matrix, *f.split('='))
# print(np.count_nonzero(matrix))

for f in fold:
    matrix = fold_matrix(matrix, *f.split('='))
    print(np.count_nonzero(matrix))

from matplotlib import pyplot as plt
f = plt.imshow(np.minimum(matrix, 1))
plt.show()