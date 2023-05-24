
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

r,c,d = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

#서 남 동 북
direction = [[0,-1],[1,0], [0,1], [-1,0]]

cnt = 0
while True:
    if li[r][c] == 0:
        cnt += 1
        li[r][c] = 2
    can_move = False
    for i in range(1, 5):
        tmp = (d+i) % 4
        search = direction[tmp]
        if 0 <= r < n and 0 <= c < m and li[r+search[0]][c+search[1]] == 0:
            d = tmp
            r += direction[tmp][0]
            c += direction[tmp][1]
            can_move = True
            break
    if not can_move:
        tmp = (d+2) % 4
        search = direction[tmp]
        if 0 <= r < n and 0 <= c < m and li[r+search[0]][c+search[1]] != 1:
            r += direction[tmp][0]
            c += direction[tmp][1]
        else:
            break

print(cnt)
