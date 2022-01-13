# https://www.hackerrank.com/challenges/30-binary-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    num = int(input().strip())
    cons_one = bin(num)[2:].split('0')
    print(len(max(cons_one)))
        