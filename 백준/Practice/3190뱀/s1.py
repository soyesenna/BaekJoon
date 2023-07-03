import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

apples = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(k)]

li = [[0 for _ in range(n)] for _ in range(n)]
for apple in apples:
    li[apple[0]][apple[1]] = 1

l = int(input())
orders = [list(input().rstrip().split()) for _ in range(l)]
time = 0

now_head = [0,0]
now_tail = [0,0]
li[0][0] = 2
now_dir = 0
#오른 아래 왼 위
direction = [[0,1], [1,0], [0,-1], [-1,0]]
for order in orders:
    num, dir = order
    num = int(num)
    for i in range(num):
        if 0 <= now_head[0] + direction[now_dir][0] < n and 0 <= now_head[1] + direction[now_dir][1] < n:
            time += 1
            now_head[0] += direction[now_dir][0]
            now_head[1] += direction[now_dir][1]
            if li[now_head[0]][now_head[1]] == 1:
                li[now_head[0]][now_head[1]] = 2
            elif li[now_head[0]][now_head[1]] == 0:
                li[now_head[0]][now_head[1]] = 2
                li[now_tail[0]][now_tail[1]] = 0
                
            else:
                #print('me')
                print(time)
                sys.exit()
        else:
            #print('wall')
            print(time + 1)
            sys.exit()
    if dir == 'D':
        now_dir = (now_dir + 1) % 4
    else:
        now_dir -= 1
        if now_dir < 0:
            now_dir += 4




