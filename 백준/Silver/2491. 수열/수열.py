import sys

def big(li):
    start = 0
    now = 1
    result = []
    while now < len(li):
        if li[now - 1] <= li[now]:
            now += 1
            if now == len(li):
                result.append(now - start)
        else:
            result.append(now - start)
            start = now
            now = start + 1

    return max(result)

def small(li):
    start = 0
    now = 1
    result = []
    while now < len(li):
        if li[now - 1] >= li[now]:
            now += 1
            if now == len(li):
                result.append(now - start)
        else:
            result.append(now - start)
            start = now
            now = start + 1

    return max(result)

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

if len(li) < 2:
    print(1)
else:
    print(max(big(li), small(li)))  