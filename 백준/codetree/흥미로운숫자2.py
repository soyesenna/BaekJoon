import sys
import collections

input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 0
for i in range(x, y + 1):
    now = str(i)
    counter = collections.Counter(now)
    if len(counter.keys()) == 2 and 1 in counter.values():
        cnt += 1
print(cnt)