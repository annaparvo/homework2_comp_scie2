#!/bin/python

def insertionSort2(ar,m):
    for i in range(m-1):
        if ar[i]>ar[i+1]:
            temp = sorted(ar[:i+2])
            ar = temp + ar[i+2:]
            print ' '.join(str(v) for v in ar)
        else:
            print ' '.join(str(v) for v in ar)

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort2(ar,m)