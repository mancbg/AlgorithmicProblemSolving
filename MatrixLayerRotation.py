#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the matrixRotation function below.
def matrix_rotation(matrix, r):
    k = min(m, n)

    for layer in range(k // 2):
        layer_elements = []

        # Collect elements in the top row in that layer
        for index in range(layer, n - 1 - layer, 1):
            layer_elements.append(matrix[layer][index])
        # Collect the right column in that layer
        for index in range(layer, m - 1 - layer):
            layer_elements.append(matrix[index][n - 1 - layer])
        # Collect the down row in that layer
        for index in range(n - 1 - layer, layer, -1):
            layer_elements.append(matrix[m - 1 - layer][index])
        # Collect the left column in that layer
        for index in range(m - 1 - layer, layer, -1):
            layer_elements.append(matrix[index][layer])

        slice_index = r % len(layer_elements)
        layer_elements = layer_elements[slice_index:] + layer_elements[:slice_index]

        counter = 0
        for index in range(layer, n - 1 - layer):
            matrix[layer][index] = layer_elements[counter]
            counter += 1
        for index in range(layer, m - 1 - layer):
            matrix[index][n - 1 - layer] = layer_elements[counter]
            counter += 1
        for index in range(n - 1 - layer, layer, -1):
            matrix[m - 1 - layer][index] = layer_elements[counter]
            counter += 1
        for index in range(m - 1 - layer, layer, -1):
            matrix[index][layer] = layer_elements[counter]
            counter += 1

    for each in matrix:
        print(*each)


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    input_matrix = []

    for _ in range(m):
        input_matrix.append(list(map(int, input().rstrip().split())))

    # m, n, r = 4, 4, 2
    # input_matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    assert m == len(input_matrix)
    assert n == len(input_matrix[0])
    matrix_rotation(input_matrix, r)
