import sys
import collections
from copy import deepcopy

input = sys.stdin.readline

n, l, r = map(int, input().split())


def in_range(now):
    global n
    return 0 <= now[0] < n and 0 <= now[1] < n


def bfs(li: list, now:list):
    global l, r
    queue = collections.deque()
    visited = []
    visited_idx = []

    queue.append(now)

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        now = queue.popleft()
        if now in visited_idx:
            continue
        visited_idx.append(now)
        visited.append(li[now[0]][now[1]])
        for d in direction:
            if in_range([now[0] + d[0], now[1] + d[1]]) and [now[0] + d[0], now[1] + d[1]] not in visited_idx and l <= abs(li[now[0]][now[1]] - li[now[0] + d[0]][now[1] + d[1]]) <= r:
                queue.append([now[0] + d[0], now[1] + d[1]])

    if len(visited) > 1:
        return sum(visited) // len(visited), visited_idx
    return -1, []

def day_start(map_:list):
    global n
    map_copy = deepcopy(map_)
    flag = False
    for i in range(n):
        for j in range(n):
            result, result_idx = bfs(deepcopy(map_), [i,j])
            if result != -1:
                flag = True
                for v in result_idx:
                    map_copy[v[0]][v[1]] = result
    return map_copy, flag



map_ = [list(map(int, input().split())) for _ in range(n)]

days = 1
while True:
    map_, flag = day_start(map_)
    if not flag:
        days -=1
        break
    days += 1

print(days)