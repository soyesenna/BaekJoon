import sys
import collections

def dfs(graph:list, root:list):
    global n
    global m

    queue = collections.deque()

    

    queue.append(root)
    cnt = 1

    flag = True
    while flag:
        cnt += 1
        for _ in range(len(queue)):
            now = queue.popleft()
            
            if now[0] == n-1 and now[1] == m-1:
                flag = False
                break
            
            dx = [0,0,1,-1]
            dy = [-1,1,0,0]
            for i in range(4):
                next = [now[0]+dy[i], now[1]+dx[i]]
                if next[0] < 0 or next[0] > n-1 or next[1] < 0 or next[1] > m-1:
                    continue
                if graph[next[0]][next[1]] == '1':
                    queue.append(next)
                    graph[now[0]][now[1]] = 'v'

    return cnt-1

n, m = map(int, sys.stdin.readline().split())

miro = []
for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())

    miro.append(tmp)

print(dfs(miro, [0,0]))