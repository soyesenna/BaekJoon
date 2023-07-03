
import sys


n = int(sys.stdin.readline())
order = list(map(int, sys.stdin.readline().split()))

def check(per_li):
    global order
    res = [0 for _ in range(len(per_li))]
    for i in range(len(per_li) - 1, -1, -1):
        for j in range(i, -1, -1):
            if per_li[i] < per_li[j]:
                res[per_li[i] - 1] += 1
    
    if res == order:
        for i in per_li:
            print(i, end=' ')
        sys.exit()

def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)

    return result

 

(perm([i for i in range(1, n + 1)], n))
