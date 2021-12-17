from helpers import *
from collections import defaultdict, Counter
import numpy as np

lines = load_file(17, test=0)[0].rstrip().replace(',', '')
lines = [line.split('=')[1].split('..') for line in lines.split()[-2:]]
xmin, xmax = [int(x) for x in lines[0]]
ymin, ymax = [int(x) for x in lines[1]]


def step(x_pos, y_pos, x_vel, y_vel):
    x_pos += x_vel
    if x_vel > 0:
        x_vel -= 1
    elif x_vel < 0:
        x_vel += 1

    y_pos += y_vel
    y_vel -= 1

    return x_pos, y_pos, x_vel, y_vel


def passed_target(x_pos, y_pos):
    return x_pos > xmax or y_pos < ymin


def inside_target(x_pos, y_pos):
    return xmin <= x_pos <= xmax and ymin <= y_pos <= ymax


best_height = -100
best_vel = None
points = []
for vx_0 in range(-100, 1000):
    for vy_0 in range(-1000, 1000):
        max_height = -100
        x_p, y_p = 0, 0
        x_v, y_v = vx_0, vy_0

        while not passed_target(x_p, y_p):
            x_p, y_p, x_v, y_v = step(x_p, y_p, x_v, y_v)

            if y_p > max_height:
                max_height = y_p

            if inside_target(x_p, y_p):
                points.append((vx_0, vy_0))
                if max_height > best_height:
                    best_height = max_height
                    best_vel = vx_0, vy_0
                    print(f'{best_height=}: {best_vel}')
                continue

# print(f'{best_height=}: {best_vel}')
print(len(set(points)))