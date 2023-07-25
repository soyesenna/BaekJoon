import sys

input = sys.stdin.readline

li = [0 for _ in range(101)]

a, b = map(int, input().split())
for i in range(a, b ):
    li[i] += 1

x, y = map(int, input().split())
for i in range(x, y):
    li[i] += 1

cnt = 0
for i in range(len(li)):
    if li[i] > 0:
       cnt += 1

print(cnt)
