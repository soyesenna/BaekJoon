import sys

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

x_min = min(map(lambda x: x[0], points)) - 1
x_max = max(map(lambda x: x[0], points)) + 1
y_min = min(map(lambda x: x[1], points)) - 1
y_max = max(map(lambda x: x[1], points)) + 1

result = 1e10+10
for i in range(x_min, x_max, 2):
    for j in range(y_min, y_max, 2):
        now = [len(list(filter(lambda x: x[0] < i and x[1] > j, points))),
               len(list(filter(lambda x: x[0] > i and x[1] > j, points))),
               len(list(filter(lambda x: x[0] > i and x[1] < j, points))),
               len(list(filter(lambda x: x[0] < i and x[1] < j, points)))]
        result = min(result, max(now))
print(result)