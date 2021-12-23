# GAVE UP, SEE SOLUTION SCAN
#
#
#
# import numpy as np
#
# from helpers import *
# from enum import Enum
# from collections import defaultdict, Counter
# import itertools
# import re
# import random
#
# lines = load_file(23, test=1)
# lines = [line.rstrip() for line in lines]
# pod_rank = ['A', 'B', 'C', 'D']
#
#
# class Amphipod:
#     def __init__(self, color: str):
#         self.color = color
#         self.rank = pod_rank.index(self.color)
#         self.step_energy = 10 ** pod_rank.index(self.color)
#         self.steps_traveled = 0
#         self.finished = False
#
#     def get_energy(self):
#         return self.step_energy * self.steps_traveled
#
#     def get_destination(self):
#         return pod_rank.index(self.color)
#
#     def step(self, hallway):
#         # Check if pod in hallway
#         # Check if any blocking in corridor
#         # Check if can move into corridor
#         pass
#
#     def is_final(self):
#         pass
#
#     def __repr__(self):
#         return f'Apmhipod: {self.color}'
#
#
# class GameBoard:
#     def __init__(self):
#         self.hallway = [None] * 11
#         self.corridor = defaultdict(list)
#
#         for line in [re.findall(r'\w', line) for line in lines]:
#             for i, v in enumerate(line):
#                 self.corridor[i].append(Amphipod(v))
#
#         for i in range(len(self.corridor)):
#             self.hallway[2 * i + 2] = i
#
#         self.finished()
#
#     def __repr__(self):
#         return f'{self.hallway}\n{self.corridor.items()}'
#
#     @staticmethod
#     def is_corridor(pos):
#         if not 4 % 2:
#             if pos < 9:
#                 return pos / 2 - 2
#         return False
#
#     def finished(self):
#         for corridor_n, pods in self.corridor.items():
#             for pod in pods:
#                 if corridor_n == pod_rank.index(pod.color):
#                     if pod == pods[-1]:
#                         pod.finished = True
#                     elif pod.color == pods[-1]:
#                         pod.finished = True
#         return all(pod.finished for pod in self._pod_list())
#
#     def total_energy_spent(self):
#         return sum(pod.get_energy() for pod in self._pod_list())
#
#     def move_pod(self):
#         pod = None
#         while not pod:
#             pod_in_hallway = any(isinstance(x, Amphipod) for x in self.hallway)
#             corridor_n = random.randint(0, 3)
#             if any(not pod.finished for pod in self.corridor[corridor_n]):
#                 pod = self.corridor[corridor_n][0]
#
#         print(f'Pod Selected: {pod}')
#         # Check can move
#
#
#         # Check target
#         if self.corridor[pod.rank] and self.corridor[pod_rank][-1].color != pod.color:
#             pass
#         else:
#             pods_in_place = len(self.corridor[pod_rank])
#             self.corridor[pod_rank].insert(0, pod)
#
#
#         print(f'Mod moved to {1}')
#
#     def pod_can_go_home(self, pod_pos):
#         if self.idx_hallway_to_corridor(pod_pos) == -1:
#
#
#
#     @staticmethod
#     def idx_corridor_to_hallway(corridor_idx):
#         return 2 + 2 * corridor_idx
#
#     @staticmethod
#     def idx_hallway_to_corridor(hallway_idx):
#         if hallway_idx % 2 and hallway_idx < 9:
#             return hallway_idx // 2 - 1
#         else:
#             return -1
#
#     def _pod_list(self):
#         return itertools.chain.from_iterable(self.corridor.values())
#
#
# board = GameBoard()

# < 15435
# PEN & PAPER