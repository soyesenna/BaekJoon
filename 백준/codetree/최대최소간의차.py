import sys
import collections

input = sys.stdin.readline

n, k = map(int, input().split())

li = list(map(int, input().split()))

now_min = min(li)
now_max = max(li)

cost = 0
while True:
    counter = collections.Counter(li)
    now_min = min(li)
    now_max = max(li)
    if now_max - now_min <= k:
        break
    if counter[now_min] > counter[now_max]:
        for i in range(len(li)):
            if li[i] == now_max:
                li[i] -= 1
                cost += 1
    else:
        for i in range(len(li)):
            if li[i] == now_min:
                li[i] += 1
                cost += 1

print(cost)
