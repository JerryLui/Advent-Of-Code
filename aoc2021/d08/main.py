from helpers import *
import numpy as np
from collections import defaultdict, Counter

lines = load_file(8)
lines = [line.strip().split('|') for line in lines]
# lines = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# """
# lines = [line.split('|') for line in lines.splitlines()]

num_map = {'acdeg': 2,
           'acdfg': 3,
           'abdfg': 5,
           'abcefg': 0,
           'abdefg': 6,
           'abcdfg': 9}

# count = 0
# for line in lines:
#     output = line[1].split()
#     for out in output:
#         if len(out) in (2, 3, 4, 7):
#             count += 1

def translate_input(input_string):
    wire_map = defaultdict(set)
    input_string = input_string.split()
    # 1
    for i in input_string:
        if len(i) == 2:
            wire_map['c'].update(list(i))
            wire_map['f'].update(list(i))

    # 7
    for i in input_string:
        if len(i) == 3:
            for c in i:
                if c not in wire_map['c']:
                    wire_map['a'].add(c)

    # 4
    for i in input_string:
        if len(i) == 4:
            for c in i:
                if c not in wire_map['c']:
                    wire_map['b'].add(c)
                    wire_map['d'].add(c)

    token_set = set()
    [token_set.update(v) for v in wire_map.values()]

    five_char_list = []
    # 5, 2, 3
    for i in input_string:
        if len(i) == 5:
            five_char_list.append(i)

    fcount = Counter()
    for five_char_str in five_char_list:
        fcount.update([c for c in five_char_str if c not in token_set])
    extracted = fcount.most_common(2)
    wire_map['g'] = {extracted[0][0]}
    wire_map['e'] = {extracted[1][0]}

    fcount = Counter()
    for five_char_str in five_char_list:
        fcount.update([c for c in five_char_str if c in wire_map['b']])
    extracted = fcount.most_common(2)
    wire_map['b'] = {extracted[1][0]}
    wire_map['d'] = {extracted[0][0]}

    # 6, 7, 9
    fcount = Counter()
    six_char_list = [i for i in input_string if len(i) == 6]
    for six_char_str in six_char_list:
        fcount.update([c for c in six_char_str if c in wire_map['c']])
    extracted = fcount.most_common(2)
    wire_map['f'] = {extracted[0][0]}
    wire_map['c'] = {extracted[1][0]}

    wire_map = dict((k, v.pop()) for k, v in wire_map.items())
    return wire_map


def str_to_num(translation_map, ast):
    if len(ast) == 2:
        return 1
    elif len(ast) == 3:
        return 7
    elif len(ast) == 4:
        return 4
    elif len(ast) == 7:
        return 8
    else:
        translated_set = set([translation_map[c] for c in ast])
        if translated_set not in [set(e) for e in num_map]:
            print(ast, translated_set)
        else:
            translated = list(translated_set)
            translated.sort()
            return num_map[''.join(translated)]


def solve_map(translation_map, output_string):
    output_string = output_string.split()
    r = ''
    for out in output_string:
        r += str(str_to_num(translation_map, out))
    return int(r)


result = 0
for line in lines:
    wire_map = translate_input(line[0])
    inv_map = {v: k for k, v in wire_map.items()}
    result += solve_map(inv_map, line[1])




# count = 0
# for line in lines:
#     output = line[1].split()
#     input_str = line[0].split()
#     print(''.join([str(translate_input(i)) for i in input_str]))
#     # count += int(''.join([str(translate(out)) for out in output]))



# def translate(astr: str):
#     if len(astr) == 2:
#         return 1
#     if len(astr) == 4:
#         return 4
#     if len(astr) == 3:
#         return 7
#     if len(astr) == 7:
#         return 8
#     if astr == 'cbgef':
#         return 5
#     if astr == 'cdgba':
#         return 2
#     if astr == 'cefdb':
#         return 3
#     if astr == 'cefbgd':
#         return 9
#     if astr == 'bcgafe':
#         return 6
#     print(astr)
#     return 0