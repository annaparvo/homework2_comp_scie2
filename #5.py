#!/bin/python
import sys

n = int(raw_input().strip())
a = []
diagleft = 0
diagright = 0
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    diagleft += int(a_temp[a_i])
    diagright += int(a_temp[- (a_i + 1)])
print abs(diagleft - diagright)