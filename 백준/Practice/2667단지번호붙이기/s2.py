import sys
import collections

def dfs(graph, root):
    stack = collections.deque()
    stack.append(root)
    visited = []

    cnt = 0
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            cnt += 1
            graph[now[0]][now[1]] = 'v'
            if now[0] > 0:
                if graph[now[0]-1][now[1]] == '1':
                    stack.append([now[0]-1, now[1]])
            if now[0] < len(graph) - 1:
                if graph[now[0]+1][now[1]] == '1':
                    stack.append([now[0]+1, now[1]])
            if now[1] > 0:
                if graph[now[0]][now[1]-1] == '1':
                    stack.append([now[0], now[1]-1])
            if now[1] < len(graph[0]) - 1:
                if graph[now[0]][now[1]+1] == '1':
                    stack.append([now[0], now[1]+1])

    return cnt

n = int(sys.stdin.readline())

apart_map = []
for _ in range(n):
    tmp = collections.deque()
    tmp.extend(sys.stdin.readline().rstrip())
    apart_map.append(tmp)
#rint(apart_map)
cnt = 0
flag = True
num_apart = []
while flag:
    flag = False
    for i in range(n):
        if flag:
            break
        for j in range(n):
            if apart_map[i][j] == '1':
                root = [i, j]
                num_apart.append(dfs(apart_map, root))
                cnt += 1
                flag = True
                break

print(cnt)
num_apart.sort()
for num in num_apart:
    print(num)