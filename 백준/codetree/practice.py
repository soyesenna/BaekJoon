import sys

input = sys.stdin.readline

n = int(input())

room_expect = [int(input()) for _ in range(n)]

result = []
for i in range(n):
    tmp = room_expect[i:] + room_expect[:i]
    sum_ = 0
    for j in range(n):
        sum_ += tmp[j] * j
    result.append(sum_)

print(min(result))
    