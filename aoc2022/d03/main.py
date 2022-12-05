from helpers import *

lines = load_file(3)
lines = [line.rstrip() for line in lines]

ss = 0
sets = []
for line in lines:
    # half = int(len(line) / 2)
    # p1 = line[:half]
    # p2 = line[half:]
    # val = set(p1).intersection(p2)
    # val = val.pop()
    #
    sets.append(set(line))
    if len(sets) == 3:
        sets.append(set(line))
        its = sets[0].intersection(sets[1]).intersection(sets[2])
        for val in its:
            if val.islower():
                ss += ord(val) - 96
            else:
                ss += ord(val) - 38
        sets = []
