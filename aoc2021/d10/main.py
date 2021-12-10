from helpers import *
import numpy as np
from collections import defaultdict, Counter

char_map = {'[': ']', '{': '}', '(': ')', '<': '>'}
# char_point = {')': 3, ']': 57, '}': 1197, '>': 25137}
char_point = {')': 1, ']': 2, '}': 3, '>': 4}


lines = load_file(10)
lines = [line.rstrip() for line in lines]
# lines = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""
# lines = [line.rstrip() for line in lines.splitlines()]

char_stack = []
score = []

for line in lines:
    line_score = 0
    for char in line:
        if char in char_map:
            char_stack.append(char)
        else:
            if char in char_map[char_stack[-1]]:
                char_stack.pop()
            else:
                # score += char_point[char]
                char_stack = []
                break
    while char_stack:
        char = char_stack.pop()
        line_score *= 5
        line_score += char_point[char_map[char]]
    if line_score:
        score.append(line_score)


score.sort()
print(np.median(score))
