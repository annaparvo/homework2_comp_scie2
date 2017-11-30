#!/bin/python
import sys


def quickSort(list):
    list.sort(key=lambda var: (len(var), var))


n = int(raw_input().strip())
unsorted = []
for unsorted_i in xrange(n):
    unsorted.append(raw_input())

quickSort(unsorted)
for y in unsorted:
    print
    y