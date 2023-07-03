import sys

input = sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

result = 1e+10

for now_max in range(max(li), 0, -1):
    cost = 0
    for i in range(len(li)):
        if li[i] > now_max:
            cost += (li[i] - now_max) ** 2

    now_min = min(li)
    total_cost = cost
    while now_max - now_min > 17:
        total_cost = cost
        now_min += 1
        for i in range(len(li)):
            if li[i] < now_min:
                total_cost += (now_min - li[i]) ** 2

    result = min(result, total_cost)
print(result)