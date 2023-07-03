import sys
import collections

t = int(sys.stdin.readline())

result = []
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    baechu = []
    for _ in range(k):
        baechu.append(list(map(int, sys.stdin.readline().split())))

    print(baechu)