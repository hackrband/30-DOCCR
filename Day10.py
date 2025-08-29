#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n)[2:]
    max_consecutive = max(len(seq) for seq in binary.split('0'))
    print(max_consecutive)
