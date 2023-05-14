import sys

n = int(sys.stdin.readline())

result = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()

    xy = [0,0]
    head = [[0,1], [1,0], [0,-1], [-1,0]]
    now_head = 0

    for i in range(len(order)):
        if order[i] == 'F':
            for j in range(2):
                xy[j] += head[now_head][j]
        elif order[i] == 'B':
            for j in range(2):
                xy[j] += head[now_head - 2][j]
        elif 