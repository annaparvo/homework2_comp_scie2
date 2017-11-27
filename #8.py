#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
arr.sort()
a = len(arr)-1
print sum(arr[:a]), sum(arr[1:])