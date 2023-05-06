import sys
import collections

n, k = map(int, sys.stdin.readline().split())

cnt = 0
before = n
while True:
    now = before * 2
    if now > k:
        now /= 2
        now += 1
    if now == k:
        break
    before = now
    cnt += 1

print(cnt)