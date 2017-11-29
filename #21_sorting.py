#!/bin/python
def partition(ar):
    pivot = ar[0]
    left = []
    right = []
    f = []
    for i in range(0, len(ar)):
        if ar[i] < pivot:
            left.append(ar[i])
        elif ar[i] > pivot:
            right.append(ar[i])
        else:
            f.append(ar[i])
    new = left + f + right
    print
    ' '.join(str(v) for v in new)


m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)