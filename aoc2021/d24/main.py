from helpers import *
from collections import defaultdict, Counter
from functools import lru_cache
from tqdm import tqdm
import re

lines = load_file(24, test=0)
lines = [line.rstrip().split() for line in lines]

pattern = re.compile(r'-?\d+')


@lru_cache(maxsize=None)
def operate(op_str, v1, v2):
    if op_str == 'add':
        return v1 + v2
    elif op_str == 'mul':
        return v1 * v2
    elif op_str == 'div':
        return v1 // v2
    elif op_str == 'mod':
        return v1 % v2
    else:
        return int(v1 == v2)


def get_value(pos_str: str):
    return int(pos_str) if pattern.findall(pos_str) else memory[pos_str]

# i[0] unbounded, i[1] <= 4, i[2] == 9, i[3] > 2, i[4] < 3, i[5] = i[4] + 7, i[6] > 7, i[7] = i[6] - 7 = < 2
# i[0] = 9
# i[1] = 4
# i[2] = 9
# i[3] = 9
# i[4] = 2
# i[5] = 9
# i[6] = 9
# i[7] = 2
# i[8] = i[3] - 2 = 7
# i[9] = 9
# i[10] = i[9] - 3 = 6
# i[11] = 1
# i[12] = i[1] + 5 = 9
# i[13] = i[0] = 9

# i[0] = 1
# i[1] = 1
# i[2] = 9
# i[3] = 3
# i[4] = 1
# i[5] = 8
# i[6] = 8
# i[7] = 1
# i[8] = 1
# i[9] = 4
# i[10] = 1
# i[11] = 1
# i[12] = 6
# i[13] = 1
11931881141161


largest_input = 0
for input_value in tqdm(range(int('94992' + '9' * 9), int('1'*14), -1)):
    input_value_list = list(str(input_value))
    if '0' in input_value_list or \
            int(input_value_list[3]) < 3 or \
            int(input_value_list[5]) != int(input_value_list[4]) + 7:
        continue

    memory = {v: 0 for v in ['w', 'x', 'y', 'z']}
    input_reading_head = 0
    for i, operation in enumerate(lines):
        op, p0 = operation[0], operation[1]
        if op == 'inp':
            memory[p0] = int(input_value_list[input_reading_head])
            input_reading_head += 1
        else:
            memory[p0] = operate(op, memory[p0], get_value(operation[2]))

    if not memory['z']:
        if input_value > largest_input:
            largest_input = input_value
            break

print(largest_input)
# {'w': 9, 'x': 0, 'y': 0, 'z': 89752275}

x = lambda i: 26*(26*(26*(i[0] + 6) + i[1] + 11) + i[2] + 5) + i[3] + 6 +  i[4] + 8
y = lambda i: sum(i) + 6 + 11 + 5 + 6 + 8
