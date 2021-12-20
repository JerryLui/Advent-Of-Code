from helpers import *
from collections import Counter
import numpy as np

lines = load_file(19, test=0)
lines = [line.rstrip() for line in lines]

scanners = []
tmp = []
for line in lines:
    if line and 'scanner' not in line:
        tmp.append(eval(line))
    elif not line:
        scanners.append(np.array(tmp))
        tmp = []
scanners.append(np.array(tmp))


s0 = scanners[0]
beacons = {tuple(s) for s in s0}
left_overs = list(range(1, len(scanners)))
relative_scanners = []
while left_overs:
    for it in left_overs:
        print(f'----- {it} -----')
        s1 = scanners[it]
        highest_count = 0
        for rotation in ((-1, 1, 1), (1, -1, 1), (1, 1, -1),
                         (-1, -1, 1), (-1, 1, -1), (1, -1, -1),
                         (1, 1, 1), (-1, -1, -1)):
            for shift in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (2, 0, 1), (1, 2, 0), (2, 1, 0)):
                distances = []
                common_axis = []

                adjusted = s1[:, shift]
                adjusted = rotation * adjusted

                for pt1 in beacons:
                    distances.append(pt1 - adjusted)

                counters = []
                for axis in range(3):
                    counter = Counter()
                    for diff in distances:
                        counter.update(diff[:, axis])
                    counters.append(counter)

                if all([c.most_common(1)[0][1] > 11 for c in counters]):
                    max_count = max([c.most_common(1)[0][1] for c in counters])
                    if max_count > highest_count:
                        highest_count = max_count

                        relative_rot = rotation
                        relative_shift = shift
                        relative_pos = [c.most_common(1)[0][0] for c in counters]
                        print(f'{it}: {relative_pos=} {relative_shift=} {relative_rot} {max_count=}')

        overlapping_beacons = set()
        if highest_count:
            for diff in distances:
                results = np.where(diff == relative_pos)
                for result in results:
                    if len(result) == 3 and all(result == result[0]):
                        overlapping_beacons.add(result[0])

            relative_scanners.append(relative_pos)
            relative_beacons = s1[:, relative_shift]
            relative_beacons = relative_beacons * relative_rot + relative_pos

            new_beacons = {tuple(s) for s in relative_beacons}
            beacons.update(new_beacons)
            print(f'{overlapping_beacons=}')
            print(f'{len(new_beacons)}')

            left_overs.remove(it)
        else:
            print('No overlap found!')

print(len(beacons))


