import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = [0]
li.extend(map(int, input().split()))

result = -1
for i in range(1, n + 1):
    sum_ = 0
    idx = i
    for _ in range(m):
        sum_ += li[idx]
        idx = li[idx]
    result = max(result, sum_)
print(result)
