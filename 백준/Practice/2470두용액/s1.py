import sys

input = sys.stdin.readline

n = int(input())
li = (sorted(list(map(int, input().split()))))

min_ = 200000000000001
result = [0,0]
for i in range(n):
    before = 200000000000001
    for j in range(n - 1, i, -1):
        now = abs(li[i] + li[j])
        if min_ > now:
            min_ = now
            result[0] = li[i]
            result[1] = li[j]
        if before < now:
            break
        before = now

print(result[0], result[1])