import sys

input = sys.stdin.readline

n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

max_x = li[0][1] // 2

for i in range(1, max_x + 1):
    now_x = i
    for j in range(len(li)):
        now_x *= 2
        if not(li[j][0] <= now_x <= li[j][1]):
            break
        if j == len(li) - 1:
            print(now_x // (2 ** len(li)))
            sys.exit()