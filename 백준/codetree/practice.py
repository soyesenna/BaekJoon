import sys
import math

def is_parallel(points: list) -> bool:
    #세 점이 같은 직선 위에 있을 경우
    if points[0][0] == points[1][0] == points[2][0]:
        return False
    elif points[0][1] == points[1][1] == points[2][1]:
        return False

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if points[i][0] == points[j][0]:
                return True
            elif points[i][1] == points[j][1]:
                return True
    return False

input = sys.stdin.readline

n = int(input())

points = [list(map(int, input().split())) for _ in range(n)]

max_tri = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if is_parallel([points[i], points[j], points[k]]):
                now_tri = abs((points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1])
                              - (points[j][0] * points[i][1] + points[k][0] * points[j][1] + points[i][0] * points[k][1]))
                max_tri = max(max_tri, now_tri)
print(max_tri)