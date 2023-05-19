import sys

def f(x, y):
    if x < y:
        return True
    return False

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(len(li) - 1, 0, -1):
    a = []
    if li[i] < li[i - 1]:
        for j in li[i:]:
            if j < li[i - 1]:
                a.append(j)
        b = max(a)
        c = li[i - 1]        
        li[li.index(b)] = c
        li[i - 1] = b

        result = li[:i] + sorted(li[i:], reverse=True)
        break


if len(result) == 0:
    print(-1)
else:
    for res in result:
        print(res, end=' ')
