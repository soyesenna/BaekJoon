import sys
import collections

_, m, k, x = map(int, sys.stdin.readline().split())

graph = {}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph.keys():
        graph[a] = []
    graph[a].append(b)

cnt = 1
queue = collections.deque()
queue.append(graph[x])
del graph[x]
result = {}
result[x] = 0
while cnt <= k:
    if len(queue) == 0:
        break
    else:
        for _ in range(len(queue)):
            now = queue.popleft()
            for i in range(len(now)):
                if now[i] not in result.keys():
                    result[now[i]] = cnt
                if now[i] in graph.keys():
                    queue.append(graph[now[i]])
                    del graph[now[i]]
    cnt += 1


result_list = []
for key in result.keys():
    if result[key] == k:
        result_list.append(key)

if result_list:
    result_list.sort()
    for i in result_list:
        print(i)
else:
    print(-1)