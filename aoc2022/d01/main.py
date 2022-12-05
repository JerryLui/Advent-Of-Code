from helpers import *

lines = load_file(1)

sums = []
curr_sum = 0
for line in lines:
    line = line.strip()
    if line:
        val = int(line)
        curr_sum += val
    else:
        sums.append(curr_sum)
        curr_sum = 0

print(max(sums))

sums.sort()
print(sum(sums[-3:]))
