#!/bin/python

import sys
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
a = 0
b = 0
c = 0
for i in arr:
  if i > 0:
    a += 1
  if i < 0:
    b += 1
  if i == 0:
    c += 1
print float(a)/n
print float(b)/n
print float(c)/n