# https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    all = ((arr[0][0])+(arr[0][1])+(arr[0][2])) + (arr[1][1]) + ((arr[2][0])+(arr[2][1])+(arr[2][2]))
            
    for x in range(1,5):
        for y in range(1,5):
            total = ((arr[x-1][y-1])+(arr[x-1][y])+(arr[x-1][y+1])) + (arr[x][y]) + ((arr[x+1][y-1])+(arr[x+1][y])+(arr[x+1][y+1]))
            if total > all:
                all = total
            
    print(all)