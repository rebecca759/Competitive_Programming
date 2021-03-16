#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    diagSum1 = 0
    diagSum2 = 0
    k = len(arr) - 1
    
    for i in range(len(arr)):
        diagSum1 += arr[i][i]
        
    for j in range(len(arr)):
        diagSum2 += arr[k][j]
        k -= 1
        
    print(diagSum1,diagSum2)
    
    return abs(diagSum1-diagSum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
