# https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import math
import os
import random
import re
import sys


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

totalSwaps = 0
for x in range(n):
    numberOfSwaps = 0
        
    for y in range(n-1):
        if a[y] > a[y+1]:
            swapper = a[y]
            a[y] = a[y+1]
            a[y+1] = swapper
            numberOfSwaps += 1
            totalSwaps += 1
        
    
    if numberOfSwaps == 0:
        break 
    
print('Array is sorted in ' + str(totalSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
