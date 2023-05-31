import sys

input = sys.stdin.readline

n, k = map(int, input().split())

bomb = [int(input()) for _ in range(n)]

explode = [-1]
for i in range(n):
    now_bomb = bomb[i]
    for j in range(n):
        if i == j:
            continue
        if now_bomb == bomb[j] and abs(i - j) <= k:
            explode.append(now_bomb)
            break

print(max(explode))
