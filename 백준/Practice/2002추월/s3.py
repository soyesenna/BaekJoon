import sys
import collections
from copy import deepcopy

input = sys.stdin.readline

n = int(input())

in_trucks = collections.deque([input().rstrip() for _ in range(n)])
out_trucks = collections.deque([input().rstrip() for _ in range(n)])

result = 0
before = ''
for i in range(n):
    if i == 0:
        before = in_trucks.popleft()
        continue
    now_in = in_trucks.popleft()
    tmp = deepcopy(out_trucks)
    for j in range(n):
        now_out = tmp.popleft()
        if before == now_out:
            before_idx = j
        elif now_in == now_out:
            if before_idx > j:
                result += 1
                break
    before = now_in


print(result)

