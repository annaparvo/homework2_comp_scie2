#!/bin/python

import sys


def timeConversion(s):
    a, b, c = s.split(':')
    a = int(a)
    if 'PM' in c:
        if a == 12:
            d = str(a)
        else:
            d = str(a + 12)
    else:
        if a == 12:
            d = '00'
        else:
            d = '0' + str(a)
    c = c[:-2]
    res = (d + ":" + b + ":" + c)

    return res


s = raw_input().strip()
result = timeConversion(s)
print(result)