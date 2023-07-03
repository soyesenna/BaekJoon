import sys

input = sys.stdin.readline

n, c, g, h = map(int, input().split())

temps = [list(map(int, input().split())) for _ in range(n)]

max_temp = max(map(lambda x: x[0], temps)) + 2

result = 0
for i in range(max_temp):
    a = 0
    for temp in temps:
        if i < temp[0]:
            a += c
        elif temp[0] <= i <= temp[1]:
            a += g
        else:
            a += h
    result = max(result, a)

print(result)