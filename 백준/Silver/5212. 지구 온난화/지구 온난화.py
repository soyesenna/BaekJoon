import sys

r, c = map(int, sys.stdin.readline().split())

def check_island(map_, index: list):
    global r, c
    direction = [[1,0], [-1,0], [0,1], [0,-1]]

    cnt = 0
    for dir in direction:
        now = [index[0] + dir[0], index[1] + dir[1]]
        if 0 <= now[0] < r and 0 <= now[1] < c:
            if map_[now[0]][now[1]] == '.':
                cnt += 1
        else:
            cnt += 1
    
    return cnt >= 3



map_ = []
for _ in range(r):
    map_.append(list(sys.stdin.readline().rstrip()))

for i in range(r):
    for j in range(c):
        if map_[i][j] == 'X':
            if check_island(map_, [i, j]):
                map_[i][j] = 'O'

after_map_index = []
for i in range(r):
    for j in range(c):
        if map_[i][j] == 'X':
            after_map_index.append([i,j])
        elif map_[i][j] == 'O':
            map_[i][j] = '.'

max_r = max(after_map_index, key=lambda x: (x[0]))[0]
min_r = min(after_map_index, key=lambda x: (x[0]))[0]
max_c = max(after_map_index, key=lambda x: (x[1]))[1]
min_c = min(after_map_index, key=lambda x: (x[1]))[1]

for i in range(min_r, max_r + 1):
    for j in range(min_c, max_c + 1):
        print(map_[i][j], end='')
    print()