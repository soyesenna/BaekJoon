def relu(x):
    if x < 0:
        return 0
    else:
        return x

n = int(input())

map = []
visit = []

for i in range(n):
    map_col = input()
    map_col_list = []
    for j in range(len(map_col)):
        map_col_list.append(int(map_col[j]))
    map.append(map_col_list)
    visit_col = [False for _ in range(n)]
    visit.append(visit_col)
queue = []
for i in range(n):
    for j in range(n):
        visit[i][j] = True
        if map[i][j] == 1:
            now = [i,j]

queue.append(now)
