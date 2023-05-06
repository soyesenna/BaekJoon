import sys
import collections

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a not in graph.keys():
        graph[a] = []
    graph[a].append(b)

cnt = 1

if 1 not in graph.keys():
    print(0)
else:
    result = set()
    queue = collections.deque()
    queue.append(graph[1])
    del graph[1]
    while cnt <= 2:
        if len(queue) == 0:
            break
        for _ in range(len(queue)):
            now = queue.popleft()
            for i in range(len(now)):
                if now[i] in graph.keys():
                    queue.append(graph[now[i]])
                    del graph[now[i]]
                result.add(now[i])
        cnt += 1
    print(len(result))