from helpers import *
from collections import defaultdict, Iterable
from tqdm import tqdm
import re

lines = load_file(22, test=0)

actions = [line.split()[0] for line in lines]
spans = [[int(e) for e in re.findall(r'-?\d+', line)] for line in lines]


def act_on_span(action: int, span: Iterable, cubes: dict):
    x0, x1, y0, y1, z0, z1 = span

    # Check for overlaps for each existing cube
    for pts, ac in cubes.copy().items():
        # Only check for spots where there is an existing cube -1/1
        if ac:
            old_x0, old_x1, old_y0, old_y1, old_z0, old_z1 = pts

            new_x0 = max(x0, old_x0)
            new_y0 = max(y0, old_y0)
            new_z0 = max(z0, old_z0)
            new_x1 = min(x1, old_x1)
            new_y1 = min(y1, old_y1)
            new_z1 = min(z1, old_z1)

            # Overlap IFF
            if new_x0 <= new_x1 and new_y0 <= new_y1 and new_z0 <= new_z1:
                # Remove that part of space
                cubes[(new_x0, new_x1, new_y0, new_y1, new_z0, new_z1)] -= ac

    if action == 1:
        cubes[(x0, x1, y0, y1, z0, z1)] += action
    return cubes


# Dict to keep track of all the volumes and its operation
space = defaultdict(int)

# Add new cubes to space and find overlaps
for i in tqdm(range(len(lines))):
    space = act_on_span(int(actions[i] == 'on'), tuple(spans[i]), space)

# Sum up all volumes MATHS
volume = 0
for pts, action in space.items():
    x0, x1, y0, y1, z0, z1 = pts
    vol = action * (x1 + 1 - x0) * (y1 + 1 - y0) * (z1 + 1 - z0)
    volume += vol

print(volume)
