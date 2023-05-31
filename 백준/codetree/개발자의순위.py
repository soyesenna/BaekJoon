import sys

input = sys.stdin.readline

k, n = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(k)]

cnt = 0
for i in range(1, n+1):
    idxs = [set() for _ in range(k)]
    for j in range(k):
        now = li[j][:li[j].index(i)]
        for r in range(len(now)):
            idxs[j].add(now[r])
    result = set([i for i in range(1, n+1)])
    for r in range(k):
        result = result & idxs[r]
    cnt += len(result)
print(cnt)