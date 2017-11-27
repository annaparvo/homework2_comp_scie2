#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    maxi = max(ar)
    return ar.count(maxi)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)