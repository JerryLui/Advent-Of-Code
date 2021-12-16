from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(16, test=0)
lines = [line.rstrip() for line in lines]

hex_map = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111""".splitlines()
hex_map = dict(line.split(' = ') for line in hex_map)
lines = ''.join([hex_map[c] for c in lines[0]])

i = 0
version_sum = 0


def parse_packet():
    global version_sum, i
    version_id = int(lines[i:i+3], 2)
    version_sum += version_id
    # print(f'{i=}: {version_id=}')
    i += 3

    operation_id = int(lines[i:i+3], 2)
    i += 3

    literals = parse_operation(operation_id)
    return literals


def parse_operation(op):
    global i
    if op == 4:
        literals = parse_literal()
        return int(literals, 2)
    else:
        label = int(lines[i])
        i += 1

        literals = []
        if label == 1:
            subpackets_amt = int(lines[i:i+11], 2)
            i += 11

            for _ in range(subpackets_amt):
                literals.append(parse_packet())
        elif label == 0:
            subpacket_length = int(lines[i:i+15], 2)
            i += 15

            i_start = i
            while i - i_start + 1 < subpacket_length:
                literals.append(parse_packet())
        literals = literals_opt(literals, op)
    return literals


def parse_literal():
    global i
    literal = ''
    has_next = True
    while has_next:
        has_next = int(lines[i])
        i += 1

        literal += lines[i:i+4]
        i += 4
    return literal


def literals_opt(literals, opt):
    tmp = []
    for literal in literals:
        tmp.append(int(literal) if isinstance(literal, str) else literal)
    literals = tmp
    if opt == 0:
        return sum(literals)
    elif opt == 1:
        tmp = 1
        for l in literals:
            tmp *= l
        return tmp
    elif opt == 2:
        return np.min(literals)
    elif opt == 3:
        return np.max(literals)
    elif opt == 5:
        return int(literals[0] > literals[1])
    elif opt == 6:
        return int(literals[0] < literals[1])
    elif opt == 7:
        return int(literals[0] == literals[1])


try:
    while i + 1 < len(lines) and lines[i:] != '0' * len(lines[i:]):
        # print(lines[i:])
        print(parse_packet())
except IndexError:
    pass

# print(version_sum)

