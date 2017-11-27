#!/bin/python
import string
import sys
n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
e = []
a = 0
for x in s:
    if x in string.ascii_lowercase:
        c = string.ascii_lowercase.index(x)
        a = c+k
    elif x in string.ascii_uppercase:
        b = string.ascii_uppercase.index(x)
        a = b+k
    a = a%26
    if x.isupper():
        e.append(string.ascii_uppercase[a])
    elif x.islower():
        e.append(string.ascii_lowercase[a])
    else:
        e.append(x)
print (''.join(e))