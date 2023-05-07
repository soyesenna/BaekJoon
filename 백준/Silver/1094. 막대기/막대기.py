import sys
import collections

x = int(sys.stdin.readline())

n_list = collections.deque([64])

while x < sum(n_list):
    low = n_list.popleft()
    n_list.appendleft(low / 2)

    if sum(n_list) < x:
        n_list.appendleft(low)

print(len(n_list))

