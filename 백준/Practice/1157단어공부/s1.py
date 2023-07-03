import sys
import collections

s = list(sys.stdin.readline().rstrip())

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        s[i] = chr((ord(s[i]) - 32))

counter = collections.Counter(s)

counter = list(counter.items())

counter.sort(key=lambda x:-x[1])

if len(counter) > 1:
    if counter[0][1] == counter[1][1]:
        print('?')
    else:
        print(counter[0][0])
else:
    print(counter[0][0])