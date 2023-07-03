import sys

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

lines = [0 for _ in range(101)]

for j in range(n):
    a, b = points[j]
    for i in range(a, b + 1):
        lines[i] += 1

cnt = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            now_point = [points[i], points[j], points[k]]
            for point in now_point:
                for r in range(point[0], point[1]+1):
                    lines[r] -= 1
            for r in range(len(lines)):
                if lines[r] > 1:
                    cnt -= 1
                    break
            cnt += 1
            for point in now_point:
                for r in range(point[0], point[1]+1):
                    lines[r] += 1
print(cnt)