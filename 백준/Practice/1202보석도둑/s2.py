import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())

dia = [list(map(int, input().split())) for _ in range(n)]
dia.sort(key=lambda x: (-x[1]))

bag = []
for _ in range(k):
    m = int(input())
    heapq.heappush(bag, m)

result = 0
while len(bag) > 0:
    now = heapq.heappop(bag)
    for i in range(n):
        if dia[i][0] <= now:
            dia[i][0] = 1000000000
            result += dia[i][1]
            break

print(result)
