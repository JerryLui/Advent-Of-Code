from helpers import *

with open(r'C:\Users\jerry\SynologyDrive\Code\Advent of Code\aoc2022\d04\input.txt', "r") as f:
    lines = f.readlines()
lines = [line.rstrip() for line in lines]


def contains(a1, a2, b1, b2):
    #if a1 <= b1 and a2 >= b2:
    if set(range(a1, a2+1)).intersection(range(b1, b2+1)):
        return True
    return False


total = 0
lst = []
for line in lines:
    a, b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    if contains(a1, a2, b1, b2): #or contains(b1, b2, a1, a2):
        total += 1