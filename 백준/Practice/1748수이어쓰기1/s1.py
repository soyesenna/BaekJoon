import sys

n = int(sys.stdin.readline())

s = ''
for i in range(1, n + 1):
    s += str(i)

print(len(s))