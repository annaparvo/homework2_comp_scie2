#!/bin/python
import sys
n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
sorted1 = []
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(int(unsorted_t))
for i in range(1, len(unsorted)):
    for j in range(0, i):
        if (unsorted[i] < unsorted[j]):
            item = unsorted.pop(i)
            unsorted.insert(j, item)
for i in unsorted:
    print i