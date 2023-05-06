import sys
import collections

def bfs(n, k):
    queue = collections.deque()
    queue.append([n, 0])

    direction = [2,1,-1]
    visited = set()
    result = 0

    while True:
        now = queue.popleft()
        if now[0] == k:
            result = now[1]
            break

        for i in direction:
            if i == 2:
                a = [now[0]*2, now[1]+1]
            elif i == 1:
                a = [now[0]+1, now[1]+1]
            else:
                a = [now[0]-1, now[1]+1]

            if a[0] not in visited and a[0] <= 100000:
                queue.append(a)
                visited.add(a[0])

    return result

n, k = map(int, sys.stdin.readline().split())

print(bfs(n,k))