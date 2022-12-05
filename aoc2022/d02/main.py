from helpers import *

lines = load_file(2)

lines = [line.split() for line in lines]
#
names = {'X': 'A', 'Y': 'B', 'Z': 'C'}
scores = {'A': 1, 'B': 2, 'C': 3}
seconds = {'X': 0, 'Y': 3, 'Z': 6}
trumps = {'B': 'A', 'C': 'B', 'A': 'C'}
reverse_trump = {v: k for k, v in trumps.items()}
#
score = 0
for line in lines:
    first = line[0]
    second = names[line[1].strip()]

    if second == 'A':
        score += scores[trumps[first]]
    elif second == 'B':
        score += scores[first]
    else:
        score += scores[reverse_trump[first]]

    # score += scores[second]
    score += seconds[line[1].strip()]

print(score)
