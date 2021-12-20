from helpers import *
from collections import Counter
import numpy as np

lines = load_file(20, test=0)
lines = [line.rstrip() for line in lines]

decoder = [int(c) for c in lines[0].replace('#', '1').replace('.', '0')]
input_array = [[int(c) for c in line.replace('#', '1').replace('.', '0')] for line in lines[2:]]

image_matrix = np.array(input_array, dtype=np.int8)


def get_input_value(matrix, x, y):
    result = matrix[x-1:x+2, y-1:y+2].flatten()
    result = ''.join(map(str, result))
    return int(result, 2)


for enhance in range(50):
    print(enhance)
    padded_matrix = np.pad(image_matrix, 3, constant_values=enhance % 2)
    size = padded_matrix.shape[0]
    if enhance % 2:
        tmp = np.zeros((size, size), dtype=np.int8)
    else:
        tmp = np.ones((size, size), dtype=np.int8)

    # print(padded_matrix[:6, :6])
    # print(padded_matrix[-6:, -6:])
    # print(padded_matrix.shape)
    # print('-'*40)

    for i in range(1, padded_matrix.shape[0] - 1):
        for j in range(1, padded_matrix.shape[1] - 1):
            tmp[i, j] = decoder[get_input_value(padded_matrix, i, j)]
    image_matrix = tmp[1:-1, 1:-1]
    # print(image_matrix[:5, :5])
    # print(image_matrix[-5:, -5:])
    # print(image_matrix.shape)
    # print('-' * 40)

print(np.sum(image_matrix))

# 54__
