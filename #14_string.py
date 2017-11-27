#!/bin/python

import sys
a = 'hackerrank'
q = int(raw_input().strip())
for a0 in xrange(q):
    b = 0
    s = raw_input().strip()
    if len(a) > len(s):
        print 'NO'
        break
    for i in range(len(s)):
        if b < len(a) and s[i]==a[b]:
            b+=1
    if b != 10:
        print 'NO'
    else:
        print 'YES'