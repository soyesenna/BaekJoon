import sys
import collections

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

digit_map = []

for _ in range(5):
    for _ in range(5):
        tmp = list(map(int, sys.stdin.readline().split()))
        digit_map.append(tmp)

