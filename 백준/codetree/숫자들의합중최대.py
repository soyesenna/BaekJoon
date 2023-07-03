import sys

input = sys.stdin.readline

x, y = map(int, input().split())

result = 0
for i in range(x, y+1):
    s = 0
    for j in range(len(str(i))):
        s += int(str(i)[j])
    result = max(s, result)

print(result)