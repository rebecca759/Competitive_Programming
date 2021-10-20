#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def stepPerms(n):
    memo = {}
    return countWays(n,memo)
    
def countWays(n,memo):
    if n in memo:
        return memo[n]
        
    if n < 0:
        return 0
        
    if n == 0 or n == 1:
        return 1
        
    memo[n] = countWays(n-1,memo)+countWays(n-2,memo)+countWays(n-3,memo)
    return memo[n]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
