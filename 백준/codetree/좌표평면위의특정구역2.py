import sys

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

result = 3000000000
for i in range(n):
    now_points = points[:i] + points[i+1:]
    max_r = 0
    min_r = 50000
    max_c = 0
    min_c = 50000
    for point in now_points:
        max_r = max(max_r, point[0])
        min_r = min(min_r, point[0])
        max_c = max(max_c, point[1])
        min_c = min(min_c, point[1])


    result = min(result, (max_r - min_r) * (max_c - min_c))

print(result)