def counting(ar):
    la = [0] * 100
    for i in ar:
        la[i] += 1
    return la

def printOrdered(arr):
    for i in range(0, 100):
        for j in range(0, arr[i]):
            print i,


m = input()
ar = [int(i) for i in raw_input().strip().split()]
printOrdered(counting(ar))