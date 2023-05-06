import sys
import collections

n = int(sys.stdin.readline())

hwak = []
for i in range(n):
    a = list(sys.stdin.readline().rstrip().split('.'))
    hwak.append(a[-1])

counter = collections.Counter(hwak)

sort_key = sorted(list(counter.keys()))

for key in sort_key:
    print(key, counter[key])