
import sys

n = int(sys.stdin.readline())

bussiness = []
for _ in range(n):
    tmp = tuple(map(int, sys.stdin.readline().rstrip().split()))
    bussiness.append(tmp)

bussiness.sort(key=lambda x: (x[1], x[0]))

now = bussiness[0]
cnt = 1
for i in range(1,n):
    if bussiness[i][0] >= now[1]:
        now = bussiness[i]
        cnt += 1
print(cnt)
