import re

from helpers import *
from collections import Counter, defaultdict
import numpy as np


lines = load_file(22, test=3)
lines = [line.rstrip() for line in lines]

actions = [line.split()[0] for line in lines]
spans = [[50 + int(e) for e in re.findall('-?\d+', line)] for line in lines]

space = np.zeros((100, 100, 100), dtype=np.ubyte)
for i, action in enumerate(actions):
    tx0, tx1, ty0, ty1, tz0, tz1 = spans[i]
    x0, x1 = sorted((tx0, tx1))
    y0, y1 = sorted((ty0, ty1))
    z0, z1 = sorted((tz0, tz1))

    space[x0: x1+1, y0:y1+1, z0:z1+1] = int(action == 'on')
    # print(action, int(action=='on'), x0, x1, y0, y1, z0, z1)
    print(np.count_nonzero(space))
