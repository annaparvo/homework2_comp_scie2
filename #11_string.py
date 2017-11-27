#CamelCase

#!/bin/python

import sys
s = raw_input().strip()
a = 1
for i in s:
    if i.isupper():
        a += 1
print a