import sys

input = sys.stdin.readline

n, k, p, t = map(int, input().split())

dev = [[False, 0] for _ in range(n + 1)]

dev[p][0] = True

for _ in range(t):
    sec, x, y = map(int, input().split())

    if dev[x][0] and dev[y][0]:
        if dev[x][1] < k:
            dev[x][1] += 1
        if dev[y][1] < k:
            dev[y][1] += 1
        continue
    
    if dev[x][0] and dev[x][1] < k:
        dev[y][0] = True
        dev[x][1] += 1
        continue
    
    if dev[y][0] and dev[y][1] < k:
        dev[x][0] = True
        dev[y][1] += 1

for i in range(1, len(dev)):
    if dev[i][0]:
        print(1, end='')
    else:
        print(0, end='')


