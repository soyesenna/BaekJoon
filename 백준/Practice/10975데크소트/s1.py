import sys
import collections

input = sys.stdin.readline

n = int(input())

deque_list = []

for _ in range(n):
    if len(deque_list) == 0:
        deque_list.append(collections.deque([int(input())]))
        continue
    now = int(input())
    deque_list.append(collections.deque([now]))
    for i in range(len(deque_list)):
        left = deque_list[i].popleft()
        right = deque_list[i].pop()
        if left > now:
            deque_list[i].appendleft(left)
            deque_list[i].append(right)
            deque_list[i].appendleft(now)
            deque_list.pop()
            break
        elif right < now:
            deque_list[i].append(right)
            deque_list[i].appendleft(left)
            deque_list[i].append(now)
            deque_list.pop()
            break


print(len(deque_list))