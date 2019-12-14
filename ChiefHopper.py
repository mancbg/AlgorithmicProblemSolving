#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the chiefHopper function below.
def chiefHopper(arr):
    # Do backward tracking
    # Assumption: energy left in the end is zero
    # so that we can get minimum value at the start
    # by going backwards
    new_energy = 0

    # Calculate energy before jumping on each building
    # starting from the last building
    for i in range(len(arr) - 1, -1, -1):
        new_energy = math.ceil((new_energy + arr[i]) / 2)

    return new_energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
