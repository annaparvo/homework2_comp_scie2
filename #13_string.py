#MarsExploration
#!/bin/python

import sys
S = raw_input().strip()
a = 0
b = [S[i:i+3] for i in range(0, len(S), 3)]
for i in b:
    if 'S' != i[0]:
        a+=1
    if 'O' != i[1]:
        a+=1
    if 'S' != i[2]:
        a+=1
print a