#Pangrams
import string
a = (raw_input().strip())
a = a.lower()
for x in string.ascii_lowercase:
    if x not in a:
        print 'not pangram'
        exit()
print 'pangram'