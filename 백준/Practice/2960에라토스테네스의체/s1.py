import sys
import collections

n, k = map(int, sys.stdin.readline().split())

li = [i for i in range(0, n + 1)]
li[0] = 1001
li[1] = 1001

cnt = 0
result = 0
while cnt < k:
    min_num = li.index(min(li))
    if li[min_num] != 1001:
        li[min_num] = 1001
        cnt += 1
        if cnt == k:
            result = min_num
            break

        for i in range(2, n + 1):
            if min_num * i > n:
                break
            if li[min_num * i] != 1001:
                li[min_num * i] = 1001
                cnt += 1
                if cnt == k:
                    result = min_num * i
                    break

print(result)