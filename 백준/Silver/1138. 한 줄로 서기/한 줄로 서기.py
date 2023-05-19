import sys

n = int(sys.stdin.readline())
if n == 1:
    print(1)
    sys.exit()

order = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(n - 2, -1, -1):
    if i == n - 2:
        if order[i] == 0:
            result.append(i + 1)
            result.append(i + 2)
        else:
            result.append(i + 2)
            result.append(i + 1)
        continue
    cnt = -1
    for j in range(len(result) + 1):
        cnt += 1
        if cnt == order[i]:
            result.insert(j, i + 1)
            break


for res in result:
    print(res, end=' ')