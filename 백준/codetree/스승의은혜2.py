import sys

input = sys.stdin.readline

n, b = map(int, input().split())

p_li = [int(input()) for _ in range(n)]
p_li.sort()

result = []
for i in range(n):
    p_li[i] //= 2
    sum_ = 0
    for j in range(n):
        sum_ += p_li[j]
        if sum_ > b:
            result.append(j)
            break
        if j == n - 1 and sum_ <= b:
            print(n)
            sys.exit()

    p_li[i] *= 2

if len(result) == 0:
    print(0)
else:
    print(max(result))