import sys
import collections

n, m = map(int, sys.stdin.readline().split())

s = []
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()

    for i in range(len(tmp)):
        s.append(tmp[:i])

for _ in range(m):
    s.append(sys.stdin.readline().rstrip())
counter = collections.Counter(s)

for val in list(counter.most_common()):
    print(val)