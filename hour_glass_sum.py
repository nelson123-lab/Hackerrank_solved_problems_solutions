#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.



def hourglassSum(arr):
    def generate_hourglass(matrix, row, column):
        sum = 0
        sum += matrix[row-1][ column-1]
        sum += matrix[row-1][column]
        sum += matrix[row-1][column+1]
        sum += matrix[row][column]
        sum += matrix[row+1][column-1]
        sum += matrix[row+1][column]
        sum += matrix[row+1][column+1]
        return sum
    max_hourglass = -63
    for i in range(1,5):
        for j in range(1,5):
            current_hourglass = generate_hourglass(arr, i ,j)
            if current_hourglass > max_hourglass:
                max_hourglass = current_hourglass
    return max_hourglass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
