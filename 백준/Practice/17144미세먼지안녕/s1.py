
import sys


input = sys.stdin.readline

r,c,t = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(r)]

cleaner = 0
for i in range(len(li)):
    if li[i][0] == -1:
        cleaner = i + 1
        break

#위 오른 아래 왼
direction = [[-1,0], [0,1], [1,0], [0,-1]]

time = 0

#오 위 왼 아
up_direction = [[0,1], [-1,0], [0,-1], [1,0]]
#오 아 왼 위
down_direction = [[0,1], [1,0], [0,-1], [-1,0]]

while time != t:
    tmp_list = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if li[i][j] > 0:
                to_move = li[i][j] // 5
                cnt = 0
                for d in direction:
                    now_r = i + d[0]
                    now_c = j + d[1]
                    if 0 <= now_r < r and 0 <= now_c < c and li[now_r][now_c] != -1:
                        tmp_list[now_r][now_c] += to_move
                        cnt += 1
                tmp_list[i][j] -= cnt * to_move
    #del tmp_list
    del now_r, now_c
    for i in range(r):
        for j in range(c):
            if li[i][j] != -1:
                li[i][j] += tmp_list[i][j]
    li_up = li[:cleaner][:]
    li_down = li[cleaner:][:]

    up_r = cleaner - 1
    up_c = 1
    down_r = cleaner
    down_c = 1
    tmp_list = [[0 for _ in range(c)] for _ in range(r)]
    now_d = 0
    while up_c != 0 or up_r != cleaner - 1:
        if not(0 <= up_r + up_direction[now_d][0] < r and 0 <= up_c + up_direction[now_d][1] < c):
            now_d = (now_d + 1) % 4
        if li[up_r][up_c] != 0:
            if not(up_r + up_direction[now_d][0] == cleaner - 1 and up_c + up_direction[now_d][1] == 0):
                tmp_list[up_r + up_direction[now_d][0]][up_c + up_direction[now_d][1]] = li[up_r][up_c]
            li[up_r][up_c] = 0

        up_r += up_direction[now_d][0]
        up_c += up_direction[now_d][1]

    now_d = 0
    while down_c != 0 or down_r != cleaner:
        if not(0 <= down_r + down_direction[now_d][0] < r and 0 <= down_c + down_direction[now_d][1] < c):
            now_d = (now_d + 1) % 4
        if li[down_r][down_c] != 0:
            if not(down_r + down_direction[now_d][0] == cleaner and down_c + down_direction[now_d][1] == 0):
                tmp_list[down_r + down_direction[now_d][0]][down_c + down_direction[now_d][1]] = li[down_r][down_c]
            li[down_r][down_c] = 0

        down_r += down_direction[now_d][0]
        down_c += down_direction[now_d][1]

    for i in range(r):
        for j in range(c):
            if li[i][j] != -1:
                li[i][j] += tmp_list[i][j]
    time += 1

result = 0
for i in range(r):
    result += sum(li[i])
print(result + 2)