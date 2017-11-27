#!/bin/python
import sys
n = int(raw_input().strip())
c = '#'
for i in range(1,n+1):
    print (c*i).rjust(n)