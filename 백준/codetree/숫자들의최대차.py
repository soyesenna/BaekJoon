import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = [int(input()) for _ in range(n)]

result = []
for i in range(min(li), max(li) + 1):
    cnt = 0
    for elem in li:
        if i <= elem <= i + k:
            cnt += 1
    result.append(cnt)
print(max(result))