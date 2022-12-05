import re

from helpers import *
from collections import deque

lines = load_file(5)
lines = [line.rstrip() for line in lines]

crates = lines[:8]
ops = lines[10:]

total = 0
lst = [deque() for _ in range(9)]
for line in crates[::-1]:
    for i in range(9):
        try:
            idx = i * 4 + 1
            if line[idx].isalpha():
                lst[i].append(line[idx])
        except:
            continue

for op in ops:
    amt, frm, to = map(int, re.findall('[0-9]+', op))
    tmpq = deque()
    for _ in range(amt):
        tmp = lst[frm-1].pop()
        tmpq.append(tmp)

    for _ in range(len(tmpq)):
        lst[to-1].append(tmpq.pop())

for l in lst:
    print(l.pop())