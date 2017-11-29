#!/bin/python
def insertionSort(ar,x):
    m=x
    a = ar[m-1]
    for i in range(x):

        if a < ar[:x][m-1]:
            ar[m] = ar[m-1]
            print ' '.join(str(v) for v in ar)
        elif a > ar[:x][m-1]:
            ar[m] = a
            if a < ar[0]:
                print ar[0]
                ar[0] = a
            print ' '.join(str(v) for v in ar)
            break
        if a < ar[0] and ar[0]==ar[:x][m-1]:
            ar[0] = ar[1]
            ar[0] = a
            print ' '.join(str(v) for v in ar)
        m = m-1


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar,m)#!/bin/python
def insertionSort(ar,x):
    m=x
    a = ar[m-1]
    for i in range(x):

        if a < ar[:x][m-1]:
            ar[m] = ar[m-1]
            print ' '.join(str(v) for v in ar)
        elif a > ar[:x][m-1]:
            ar[m] = a
            if a < ar[0]:
                print ar[0]
                ar[0] = a
            print ' '.join(str(v) for v in ar)
            break
        if a < ar[0] and ar[0]==ar[:x][m-1]:
            ar[0] = ar[1]
            ar[0] = a
            print ' '.join(str(v) for v in ar)
        m = m-1


m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar,m)