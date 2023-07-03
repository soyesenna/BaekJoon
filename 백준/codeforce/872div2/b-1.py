import re
import sys
 
t = int(sys.stdin.readline())
 
result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
 
    row = min(n, m)
    col = max(n, m)
 
    li.sort(reverse=True)
    #print(li)

    cnt_minus = 0
    
    for a in li:
        if a < 0:
            cnt_minus += 1
    
    if cnt_minus % 2 == 0:

        minus = []
    
        for j in range(1, len(li)):
            minus.append(li[0] - li[j])
        #print(minus)
        max_minus = max(minus)
        del minus[minus.index(max_minus)]
        se_max_minus = max(minus)
    
        res = max_minus * (col - 1) * row
        res += se_max_minus * (row - 1)
    else:
        minus = []
    
        for j in range(len(li) - 1, -1, -1):
            minus.append(abs(li[-1] - li[j]))
        #print(minus)
        max_minus = max(minus)
        del minus[minus.index(max_minus)]
        se_max_minus = max(minus)
    
        res = max_minus * (col - 1) * row
        res += se_max_minus * (row - 1)
 
    result.append(res)
 
for res in result:
    print(res)