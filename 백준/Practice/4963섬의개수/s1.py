import sys
import collections

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(graph, root):
    global dx
    global dy
    global w
    global h
    if root[0] < 0 or root[1] < 0 or root[0] > h-1 or root[1] > w-1:
        return
    if graph[root[0]][root[1]] != 1:
        return
    graph[root[0]][root[1]] = 2
    for i in range(8):
        dfs(graph, [root[0]+dy[i], root[1]+dx[i]])

   
            
result = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    island_map = []
    for _ in range(h): 
        island_map.append(list(map(int, sys.stdin.readline().split())))
    
    cnt = 0
    flag = True
    while flag:
        flag = False
        for i in range(h):
            if flag:
                break
            for j in range(w):
                if island_map[i][j] == 1:
                    dfs(island_map, [i, j])
                    cnt += 1
                    flag = True
                    break
    result.append(cnt)

for res in result:
    print(res)