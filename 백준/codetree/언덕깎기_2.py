import sys

input = sys.stdin.readline

n = int(input())

li = [int(input()) for _ in range(n)]

now_max = max(li)
now_min = min(li)

result = []
cost = 0
while now_max - now_min > 17:
    if (now_max - now_min - 17) % 2 == 0:
        minus = (now_max - now_min - 17) // 2
        for i in range(len(li)):
            if li[i] == now_max:
                li[i] -= minus
                cost += minus ** 2
            elif li[i] == now_min:
                li[i] += minus
                cost += minus ** 2
    else:
        max_cnt = len(list(filter(lambda x: x == now_max, li)))
        min_cnt = len(list(filter(lambda x: x == now_min, li)))
        minus = (now_max - now_min - 17) // 2
        if max_cnt >= min_cnt:
            for i in range(len(li)):
                if li[i] == now_max:
                    li[i] -= minus
                    cost += minus ** 2
                elif li[i] == now_min:
                    li[i] += minus + 1
                    cost += (minus + 1) ** 2
        else:
            for i in range(len(li)):
                if li[i] == now_max:
                    li[i] -= minus
                    cost += (minus + 1) ** 2
                elif li[i] == now_min:
                    li[i] += minus
                    cost += minus ** 2
    now_max = max(li)
    now_min = min(li)

print(cost)