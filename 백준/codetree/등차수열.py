import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

min_ = min(li)
max_ = max(li)

result = 0
for i in range(min_, max_ + 1):
    cnt = 0
    for j in range(n):
        for k in range(j + 1, n):
            if abs(i - li[k]) == abs(i - li[j]):
                cnt += 1
    result = max(result, cnt)

print(result)