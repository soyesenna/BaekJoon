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
    max_num = li[0]
    min_num = li[-1]

    minus = []
    for i in range(1, len(li) - 1):
        minus.append(li[0] - li[i])

    for i in range(len(li) - 2, 0, -1):
        minus.append(abs(li[-1] - li[i]))

    minus.sort()
    #print(minus)
    res = (max_num - min_num) * (col - 1) * row
    res += minus[-1] * (row - 1)


    
    
 
    result.append(res)
 
for res in result:
    print(res)