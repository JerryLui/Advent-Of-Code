from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(12)
lines = [line.rstrip() for line in lines]

# lines = """start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""".splitlines()
# lines = """dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""".splitlines()
# lines = """fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW""".splitlines()
tmp = defaultdict(list)
for line in lines:
    s, e = line.split('-')
    if e != 'start':
        tmp[s].append(e)
    if s != 'start' and e != 'end':
        tmp[e].append(s)
lines = tmp


path_lst = []


def search(graph: dict, current: str, visited: set, path: list, twice=False):
    global path_lst
    path.append(current)
    if current.islower():
        visited.add(current)

    if current == 'end':
        path_lst.append(path)
    else:
        for v in graph[current]:
            if v not in visited:
                search(graph, v, visited.copy(), path.copy(), twice)
            elif twice:
                search(graph, v, visited.copy(), path.copy(), False)


search(lines, 'start', set(), [], twice=True)
print(len(path_lst))



