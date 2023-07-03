import sys
import collections

def bfs(graph, root):
    visited = []
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue += graph[node] - set(visited)

    return visited

n = int(sys.stdin.readline())
graph = {}
for i in range(n):
    graph[i+1] = []

g_num = int(sys.stdin.readline())

for i in range(g_num):
    tmp_ = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[tmp_[0]].append(tmp_[1])
    
for key in graph:
    for i in range(len(graph[key])):
        tmp = graph[key][i]

        graph[tmp].append(key)

for key in graph:
    graph[key] = set(graph[key])

print(len(bfs(graph, 1)) - 1)
