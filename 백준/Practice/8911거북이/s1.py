import sys

n = int(sys.stdin.readline())

result = []

for _ in range(n):
    order = sys.stdin.readline().rstrip()

    xy = [0,0]
    head = [[0,1], [1,0], [0,-1], [-1,0]]
    now_head = 0
    maxs = [0,0]
    mins = [0,0]

    for i in range(len(order)):
        if order[i] == 'F':
            for j in range(2):
                xy[j] += head[now_head][j]
            maxs[0] = max(maxs[0], xy[0])
            maxs[1] = max(maxs[1], xy[1])
            mins[0] = min(mins[0], xy[0])
            mins[1] = min(mins[1], xy[1])
        elif order[i] == 'B':
            for j in range(2):
                xy[j] += head[now_head - 2][j]
            maxs[0] = max(maxs[0], xy[0])
            maxs[1] = max(maxs[1], xy[1])
            mins[0] = min(mins[0], xy[0])
            mins[1] = min(mins[1], xy[1])
        elif order[i] == 'L':
            now_head -= 1
            if now_head < 0:
                now_head += 4
        elif order[i] == 'R':
            now_head += 1
            if now_head > 3:
                now_head %= 4
    result.append([maxs, mins])

for res in result:
    if res[0][0] == 0 and res[1][0] == 0 or res[0][1] == 0 and res[1][1] == 0:
        print(0)
    else:
        print(abs(res[0][0] - res[1][0]) * abs(res[0][1] - res[1][1]))
