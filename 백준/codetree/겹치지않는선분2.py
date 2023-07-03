import sys

input = sys.stdin.readline

n = int(input())

lines = []

for _ in range(n):
    x1,x2 = map(int, input().split())
    lines.append([tuple([x1,0]), tuple([x2,1])])

cross = set()
for i in range(n):
    now_line = lines[i]
    extra = lines[:i] + lines[i+1:]
    flag = True
    for j in range(n-1):
        if extra[j][0] < now_line[0] and extra[j][1] > now_line[1]:
            cross.add(tuple(extra[j]))
            cross.add(tuple(now_line))

print(n - len(cross))