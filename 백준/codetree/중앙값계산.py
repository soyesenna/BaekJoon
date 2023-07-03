import sys

input = sys.stdin.readline
n = int(input())
li = (list(map(int, input().split())))

res = []
for i in range(n):
    if (i + 1) % 2 != 0:
        if i == 0:
            res.append(li[i])
            continue
        tmp = sorted(li[:i +1])
        res.append(tmp[i // 2])

for r in res:
    print(r, end=' ')