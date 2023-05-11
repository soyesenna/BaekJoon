
import sys

n = int(sys.stdin.readline())

x = []
y = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    x.append(tmp[0])
    y.append(tmp[1])

max_x = max(x)
min_x = min(x)
max_y = max(y)
min_y = min(y)
result = ((max_x + 10 - min_x) * 2) + ((max_y + 10 - min_y) * 2)

if (max_x) - (min_x + 10) > 0 and (max_y) - (min_y + 10) > 0:
    result += (((max_x) - (min_x + 10)) * 2) + ((max_y) - (min_y + 10)) * 2
print(result)