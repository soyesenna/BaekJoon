import sys
import heapq

n = int(sys.stdin.readline())

s = []
for _ in range(n):
    for j in list(map(int, sys.stdin.readline().rstrip().split())):
        heapq.heappush(s, -j)

for i in range(n-1):
    heapq.heappop(s)

print(-heapq.heappop(s))