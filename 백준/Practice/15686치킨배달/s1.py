import sys
import collections
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())

map_ = [list(map(lambda x: [int(x), 0], input().split())) for _ in range(n)]

chicken = []


for i in range(n):
    for j in range(n):
        if map_[i][j][0] == 2:
            chicken.append([i, j])

combinations = list(itertools.combinations(chicken, m))

result = []

for com in combinations:
    tmp = []
    for i in range(n):
        for j in range(n):
            if map_[i][j][0] == 1:
                tmp2 = []
                for c in com:
                    tmp2.append(abs(c[0] - i) + abs(c[1] - j))
                tmp.append(min(tmp2))
    result.append(sum(tmp))

print(min(result))
