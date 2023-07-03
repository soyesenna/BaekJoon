import sys

n, m = map(int, sys.stdin.readline().split())

class_map = []

for _ in range(n):
    class_map.append(sys.stdin.readline().rstrip())

max_val = min(n, m) - 1

result = 0

while max_val > 0:
    for i in range(n - max_val):
        for j in range(m - max_val):
            now = class_map[i][j]
            if class_map[i][j + max_val] == now and class_map[i + max_val][j + max_val] == now and class_map[i + max_val][j] == now:
                print((max_val + 1) ** 2)
                sys.exit()
    max_val -= 1

print(1)