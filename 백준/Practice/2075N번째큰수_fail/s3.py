import sys
import collections

n = int(sys.stdin.readline())

deq = collections.deque()
a = []
for i in range(n):
    if i == 0:
        a = list(map(int, sys.stdin.readline().split()))
        #a.sort(reverse=True)
    else:
        tmp = list(map(int, sys.stdin.readline().split()))
        