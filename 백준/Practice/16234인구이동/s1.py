import sys
import collections
from copy import deepcopy

input = sys.stdin.readline

n, l, r = map(int, input().split())


def in_range(now):
    global n
    return 0 <= now[0] < n and 0 <= now[1] < n


def bfs(li: list, now:list, visit_flag: list):
    global l, r
    queue = collections.deque()
    visited = []
    visited_idx = []

    queue.append(now)
    visit_flag[now[0]][now[1]] = True

    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        now = queue.popleft()

        visited_idx.append(now)
        visited.append(li[now[0]][now[1]])

        for d in direction:
            if in_range([now[0] + d[0], now[1] + d[1]]) and not visit_flag[now[0] + d[0]][now[1] + d[1]] and l <= abs(li[now[0]][now[1]] - li[now[0] + d[0]][now[1] + d[1]]) <= r:
                queue.append([now[0] + d[0], now[1] + d[1]])
                visit_flag[now[0] + d[0]][now[1] + d[1]] = True

    if len(visited) > 1:
        return sum(visited) // len(visited), visited_idx, visit_flag
    return -1, [], []

def day_start(map_:list):
    global n
    map_copy = deepcopy(map_)
    flag = False
    visit_flag = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(False)
        visit_flag.append(tmp)

    for i in range(n):
        for j in range(n):
            if not visit_flag[i][j]:
                result, result_idx, result_flag = bfs(deepcopy(map_), [i,j], deepcopy(visit_flag))
                if result != -1:
                    flag = True
                    for v in result_idx:
                        map_copy[v[0]][v[1]] = result
                    visit_flag = result_flag

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