import sys

input = sys.stdin.readline

a, b = map(int, input().split())
n,m = map(int, input().split())
li = [[-1 for _ in range(a)] for _ in range(b)]

#오른 아래 왼 위
#왼 아래 오른 위
direction = [[0,-1], [1,0], [0,1], [-1,0]]

robots = []
for i in range(n):
    c,r,d = input().split()
    if d == 'E':
        d = 2
    elif d == 'S':
        d = 3
    elif d == 'W':
        d = 0
    else:
        d = 1
    r = int(r) - 1
    c = int(c) - 1
    li[r][c] = d
    robots.append([r,c])

orders = [list(input().split()) for _ in range(m)]

for i in range(m):
    num, order, repeat = orders[i]

    num = int(num)

    r,c = robots[num-1]
    for _ in range(int(repeat)):
        if order == 'L':
            li[r][c] -= 1
            if li[r][c] < 0:
                li[r][c] += 4
        elif order == 'R':
            li[r][c] = (li[r][c] + 1) % 4
        else:
            move_r = direction[li[r][c]][0]
            move_c = direction[li[r][c]][1]
            r += move_r
            c += move_c
            if not(0 <= r < b and 0 <= c < a):
                print("Robot %d crashes into the wall"%(num))
                sys.exit()
            elif li[r][c] != -1:
                confilct = robots.index([r,c])
                print("Robot %d crashes into robot %d"%(num, confilct+1))
                sys.exit()
            else:
                before_r = r - move_r
                before_c = c - move_c
                li[r][c] = li[before_r][before_c]
                li[before_r][before_c] = -1
                robots[num-1] = [r,c]

print("OK")