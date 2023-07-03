import sys
import math

def is_parallel(points: list) -> list:
    #세 점이 같은 직선 위에 있을 경우
    if points[0][0] == points[1][0] == points[2][0]:
        return [False,-1]
    elif points[0][1] == points[1][1] == points[2][1]:
        return [False,-1]

    for i in range(len(points)):
        now = points[i]
        extra = points[:i] + points[i+1:]
        if extra[0][0] == extra[1][0]:
            if extra[0][1] == now[1] or extra[1][1] == now[1]:
                return [True, abs(extra[0][1] - extra[1][1]) * abs(extra[0][0] - now[0])]
        elif extra[0][1] == extra[1][1]:
            if extra[0][0] == now[0] or extra[1][0] == now[0]:
                return [True, abs(extra[0][0] - extra[1][0]) * abs(extra[0][1] - now[1])]
    return [False, -1]

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

max_tri = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            tmp = is_parallel([points[i], points[j], points[k]])
            if tmp[0]:
                max_tri = max(max_tri, tmp[1])
print(max_tri)