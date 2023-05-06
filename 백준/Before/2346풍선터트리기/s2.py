import sys
import collections

n = int(sys.stdin.readline())

my_deque = collections.deque(enumerate(((list(map(int, sys.stdin.readline().split()))))))
result_list = []
idx = 0

while my_deque:
    now = my_deque.popleft()
    result_list.append(now[0] + 1)
    if now[1] > 0:
        my_deque.rotate(-(now[1] - 1))
    else:
        my_deque.rotate(-(now[1]))

for i in result_list:
    print(i, end=' ')