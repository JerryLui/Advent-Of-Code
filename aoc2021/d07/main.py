from helpers import *
import numpy as np

lines = load_file(7)
lines = np.array([int(l) for l in lines[0].split(',')])
# lines = [16,1,2,0,4,2,7,1,2,14]
# lines = np.array(lines)


# def get_steps(steps):
#     n = steps
#     return n * (n + 1) / 2
    # return np.sum(range(1, steps+1))


def count_fuel(position):
    return np.sum([np.abs(line-position) for line in lines])


# least_fuel = np.inf
# for i in range(np.max(lines)):
#     print(i)
#     fuel = count_fuel(i)
#     if fuel < least_fuel:
#         least_fuel = fuel

# print(least_fuel)
#95851339

# P1 Median
for i in range(100):
    print(f'Run {i}')
    lines = np.random.randint(1000, size=2000, dtype=np.uint16)

    least_fuel = np.inf
    least_fuel_pos = None
    for j in range(np.max(lines)):
        fuel = count_fuel(j)
        if fuel < least_fuel:
            least_fuel = fuel
            least_fuel_pos = j

    print('Median:', int(np.median(lines)), 'Measured:', least_fuel_pos)
