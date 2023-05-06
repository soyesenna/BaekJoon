import sys
import collections

def bfs(graph, root):
    queue = collections.deque()
    queue.append(root)

    while queue:
        now = queue.pop()
        graph[now[0]][now[1]] = 'v'
        if now[0] > 0:
            if graph[now[0]-1][now[1]] == 1:
                queue.append([now[0]-1, now[1]])
        if now[0] < len(graph) - 1:
            if graph[now[0]+1][now[1]] == 1:
                queue.append([now[0]+1, now[1]])
        if now[1] > 0:
            if graph[now[0]][now[1]-1] == 1:
                queue.append([now[0], now[1]-1])
        if now[1] < len(graph[0]) - 1:
            if graph[now[0]][now[1]+1] == 1:
                queue.append([now[0], now[1]+1])


t = int(sys.stdin.readline())

result = []
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    map_ = [[0]*m for _ in range(n)]

    for _ in range(k):
        row, col = map(int, sys.stdin.readline().split())

        map_[col][row] = 1
    
    cnt = 0
    flag = True
    while flag:
        flag = False
        for i in range(n):
            if flag:
                break
            for j in range(m):
                if map_[i][j] == 1:
                    root = [i, j]
                    bfs(map_, root)
                    cnt += 1
                    flag = True
                    break
    
    result.append(cnt)

for res in result:
    print(res)
    