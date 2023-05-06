import sys
import collections

n = int(sys.stdin.readline())

right_list = []
left_list = []

li = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    li.append(tmp)

max_index = max(li, key=lambda x: x[1])[0]
deq = collections.deque(sorted(li, key=lambda x : x[0]))

