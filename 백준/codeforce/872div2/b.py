import re
import sys

t = int(sys.stdin.readline())

result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))

    row = min(n, m)
    col = max(n, m)

    cnt_minus = 0
    
    for a in li:
        if a < 0:
            cnt_minus += 1

    if cnt_minus % 2 == 0:
        max_num = max(li)
        min_num = min(li)
        del li[li.index(min_num)]
        se_min_num = min(li)    

        res = (max_num - min_num) * (col - 1) * row
        res += (max_num - se_min_num) * (row - 1)

    else:
        min_num = min(li)
        max_num = max(li)
        del li[li.index(max_num)]
        se_max_num = max(li)

        res = (max_num - min_num) * (col - 1) * row
        res += (se_max_num - min_num) * (row - 1)
    result.append(res)

for res in result:
    print(res)