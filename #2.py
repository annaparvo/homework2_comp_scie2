#!/bin/python

import sys
def simpleArraySum(n, arr):
    return sum(arr)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print simpleArraySum(n, arr)