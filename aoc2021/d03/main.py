from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

lines = [l.strip() for l in lines]
lines_length = len(lines[0])
gcount = {i: dict() for i in range(lines_length)}

for line in lines:
    for j in range(lines_length):
        gcount[j][line[j]] = gcount[j].get(line[j], 0) + 1

gamma = ['0'] * lines_length
epsilon = ['0'] * lines_length
for k, v in gcount.items():
    if v['0'] <= v['1']:
        gamma[k] = '1'
    else:
        epsilon[k] = '1'

ans1 = int(''.join(gamma), 2) * int(''.join(epsilon), 2)

## 2
oxy_cache = defaultdict(list)
co2_cache = defaultdict(list)

look_for = '0'
if gcount[0]['0'] <= gcount[0]['1']:
    look_for = '1'

for line in lines:
    if line[0] == look_for:
        oxy_cache[0].append(line)
    else:
        co2_cache[0].append(line)

def counter(lines, pos):
    count = [0, 0]
    for line in lines:
        if line[pos] == '0':
            count[0] += 1
        else:
            count[1] += 1
    return '1' if count[0] <= count[1] else '0'


for i in range(1, lines_length):
    look_for = counter(oxy_cache[i-1], i)
    for line in oxy_cache[i-1]:
        if line[i] == look_for:
            oxy_cache[i].append(line)

for i in range(1, lines_length):
    look_for = counter(co2_cache[i-1], i)
    for line in co2_cache[i-1]:
        if line[i] != look_for:
            co2_cache[i].append(line)

ans2 = int(oxy_cache[11][0], 2) * int(co2_cache[8][0], 2)
