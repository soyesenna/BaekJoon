import sys
import collections

n = int(sys.stdin.readline())

wall_deque = []

max_height = 0
max_index = 0
max_list_index = 0

for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[1] >= max_height:
        max_height = a[1]
        max_index = a[0]
    wall_deque.append(a)

wall_deque = sorted(wall_deque)
max_list_index = wall_deque.index([max_index, max_height])
left_deque = collections.deque(wall_deque[:max_list_index])
right_deque = collections.deque(wall_deque[max_list_index:])
result = max_height

if len(left_deque) != 0:
    now_wall = left_deque.popleft()

    for i in range(len(left_deque)):
        tmp_wall = left_deque.popleft()
        if now_wall[1] < tmp_wall[1]:
            result += (tmp_wall[0] - now_wall[0]) * (now_wall[1])
            now_wall = tmp_wall

    result += (max_index - now_wall[0]) * (now_wall[1])

if len(right_deque) != 0:
    now_wall = right_deque.pop()
    for i in range(len(right_deque)):
        tmp_wall = right_deque.pop()

        if now_wall[1] < tmp_wall[1]:
            result += (now_wall[0] - tmp_wall[0]) * (now_wall[1])
            now_wall = tmp_wall

print(result)
