import re
import sys

n = int(sys.stdin.readline())

xys = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    xys.append(tmp)

xys.sort(key = lambda x: (x[0], x[1]))

for res in xys:
    print(res[0], res[1])