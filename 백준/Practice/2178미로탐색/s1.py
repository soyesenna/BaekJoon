import sys
import collections

'''
bfs에서 visited처리를 popleft바로 다음에 하게되면
큐는 선입선출 방식이기때문에 선입선출 방식에따라
여러 정점이 하나의 정점을 동시에 방문하여 큐에 들어가게 된다.
이러면 여러번 방문한 정점이 또 중복된 정점들을 방문하게되고 
방문처리리스트와 큐의 크기가 기하급수적으로 커진다. -> 시간초과나 메모리초과 오류 발생
'''

def dfs(graph:list, root:list):
    global n
    global m

    queue = collections.deque()
    visited = set()

    dx = [0,0,1,-1]
    dy = [-1,1,0,0]

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
            
            
            for i in range(4):
                next = [now[0]+dy[i], now[1]+dx[i]]
                if next[0] < 0 or next[0] > n-1 or next[1] < 0 or next[1] > m-1:
                    continue
                if graph[next[0]][next[1]] == '1' and tuple(next) not in visited:
                    queue.append(next)
                    visited.add(tuple(next))
            

    return cnt-1

n, m = map(int, sys.stdin.readline().split())

miro = []
for i in range(n):
    miro.append(sys.stdin.readline().rstrip())

print(dfs(miro, [0,0]))