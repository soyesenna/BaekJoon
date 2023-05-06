import sys
import heapq

n = int(sys.stdin.readline())
num = []

result = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(num) != 0:
            result.append(heapq.heappop(num))
        else:
            result.append(0)
    else:
        heapq.heappush(num, x)

for i in result:
    print(i)