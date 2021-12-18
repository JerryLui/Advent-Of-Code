from helpers import *
import math
import re


lines = load_file(18, test=0)
lines = [eval(line.rstrip()) for line in lines]


class Node:
    def __init__(self, element, parent=None):
        self.parent = parent
        self.depth = parent.depth + 1 if parent else 0

        if isinstance(element, list):
            self.is_pair = True
            self.left, self.right = [Node(n, self) for n in element]
        elif isinstance(element, Node):
            self.is_pair = element.is_pair
            if self.is_pair:
                self.left, self.right = Node(element.left, self), Node(element.right, self)
            else:
                self.val = element.val
        else:
            self.val = element
            self.is_pair = False

    def __repr__(self):
        if self.is_pair:
            return f'{self.left, self.right}'
        else:
            return str(self.val)

    def find_explode(self):
        if self.is_pair:
            if self.depth >= 4:
                return self
            return self.left.find_explode() or self.right.find_explode()
        return False

    def find_split(self):
        if not self.is_pair:
            if self.val > 9:
                return self
            return False
        return self.left.find_split() or self.right.find_split()

    def get_first_left_val(self):
        if self.is_pair:
            return self.left.get_first_left_val() or self.right.get_first_left_val()
        return self

    def get_first_right_val(self):
        if self.is_pair:
            return self.right.get_first_right_val() or self.left.get_first_right_val()
        return self

    def explode(self):
        while n := self.find_explode():
            if first_left := get_left_neighbour(n.parent, n):
                first_left.val += n.left.val
            if first_right := get_right_neighbour(n.parent, n):
                first_right.val += n.right.val
            n.is_pair = False
            n.val = 0
            return True
        return False

    def split(self):
        while n := self.find_split():
            n.is_pair = True
            n.left = Node(math.floor(n.val/2), n)
            n.right = Node(math.ceil(n.val/2), n)
            return True
        return False

    def reduce(self):
        while True:
            if not self.explode() and not self.split():
                break

    def magnitude(self):
        if not self.is_pair:
            return self.val
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def get_left_neighbour(parent, node):
    if not parent:
        return False
    if parent.left == node:
        return get_left_neighbour(parent.parent, parent)
    else:
        return parent.left.get_first_right_val()


def get_right_neighbour(parent, node):
    if not parent:
        return False
    if parent.right == node:
        return get_right_neighbour(parent.parent, parent)
    else:
        return parent.right.get_first_left_val()


# node = Node(lines[0])
# for line in lines[1:]:
#     node = Node([node, Node(line)])
#     node.reduce()
# print(node.magnitude())

largest_sum = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            node = Node([lines[i], lines[j]])
            node.reduce()
            mag = node.magnitude()
            if mag > largest_sum:
                largest_sum = mag


