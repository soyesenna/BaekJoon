import sys
import collections

n = int(sys.stdin.readline())

cost = []

for _ in range(n):
    cost.append(list(map(int, sys.stdin.readline().rstrip().split())))


result = min(cost[0])
before = cost[0].index(min(cost[0]))
for i in range(1, n):
    if cost[i].index(min(cost[i])) == before:
        del cost[i][cost[i].index(min(cost[i]))]
    result += min(cost[i])
    before = cost[i].index(min(cost[i]))

print(result)