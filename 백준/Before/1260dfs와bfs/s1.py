import sys
import collections

def dfs(graph, root):
    visited = []
    stack = collections.deque([root])

    for key in graph:
        graph[key] = sorted(graph[key], reverse=True)

    #print(graph)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i in graph[node]:
                if i not in visited:
                    stack.append(i)

    return visited

def bfs(graph, root):
    visited = []
    queue = collections.deque([root])

    for key in graph:
        graph[key] = sorted(graph[key], reverse=False)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in graph[node]:
                if i not in visited:
                    queue.append(i)

    return visited

n, m, root = map(int, sys.stdin.readline().rstrip().split())

graph = {}
for i in range(n):
    graph[i+1] = []

for i in range(m):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    if tmp[1] not in graph[tmp[0]]:
        graph[tmp[0]].append(tmp[1])
    if tmp[0] not in graph[tmp[1]]:
        graph[tmp[1]].append(tmp[0])

'''for key in graph:
    graph[key] = list(graph[key]).sort()'''

for i in dfs(graph, root):
    print(str(i), end=' ')

print('\n', end='')
for i in bfs(graph, root):
    print(str(i), end=' ')
