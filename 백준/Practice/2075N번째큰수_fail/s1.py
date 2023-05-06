import sys
import collections

n = int(sys.stdin.readline())

mapping = {}
for i in range(n):
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(n):
        mapping[s[j]] = str(i)+str(j)

mapping = sorted(mapping.items())

print(mapping)