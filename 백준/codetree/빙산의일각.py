import sys

input = sys.stdin.readline

n = int(input())

h = [int(input()) for _ in range(n)]

min_ = min(h) - 1
max_ = max(h) + 1

result = 0
for i in range(min_, max_ + 1):
    tmp = h[::]
    for j in range(n):
        tmp[j] -= i
        if tmp[j] < 0:
            tmp[j] = 0
        else:
            tmp[j] = 1
        tmp[j] = str(tmp[j])

    a = ''.join(tmp).split('0')
    result = max(result, len(list(filter(lambda x: x != '', a))))
print(result)
