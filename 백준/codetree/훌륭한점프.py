import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = list(map(int, input().split()))

idx = 0
result = [li[0]]
while idx < n - 1:
    tmp = li[idx + 1: idx + 1 + k]
    for i in range(len(tmp) - 1, -1, -1):
        if tmp[i] == min(tmp):
            idx += i + 1
            break
    result.append(li[idx])

print(max(result))