import sys

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

min_dist = 1000000
for i in range(n):
    for j in range(i+1, n):
        min_dist = min(min_dist, ((points[i][0] - points[j][0]) ** 2) + ((points[i][1] - points[j][1]) ** 2))

print(min_dist)