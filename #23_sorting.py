n = int(raw_input())
list1 = raw_input().split()


def countingsort1(list1, n):
    idct = [0] * 100
    for i in (int(x) for x in list1):
        idct[i] += 1
    print
    ' '.join(str(v) for v in idct)


countingsort1(list1, n)