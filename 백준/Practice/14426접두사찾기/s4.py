import sys

n, m = map(int, sys.stdin.readline().split())

s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())

pre = []
for _ in range(m):
    pre.append(sys.stdin.readline().rstrip())


result = 0
for pre_str in pre:
    for line in s:
        if line.startswith(pre_str):
            result += 1
            break

print(result)