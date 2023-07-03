import sys

input = sys.stdin.readline

n = int(input())

def check(li: list):
    global n
    flag = False
    start = -10000000000
    result = []
    for i in range(n):
        if li[i] == '1':
            result.append(i - start)
            start = i
    return min(result)


li = list(input().rstrip())

res = []
for i in range(n):
    if li[i] == '0':
        li[i] = '1'
        for j in range(i + 1, n):
            if li[j] == '0':
                li[j] = '1'
                res.append(check(li))
                li[j] = '0'
        li[i] = '0'
print(max(res))