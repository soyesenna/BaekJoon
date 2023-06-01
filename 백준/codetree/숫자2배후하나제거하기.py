import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

result = 1e10+10
for i in range(n):
    li[i] *= 2
    for j in range(n):
        now = li[:j] + li[j+1:]
        tmp = 0
        for k in range(n-2):
            tmp += abs(now[k] - now[k+1])
        result = min(result, tmp)
    li[i] //= 2

print(result)