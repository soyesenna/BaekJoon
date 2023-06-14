import sys

input = sys.stdin.readline

n, k = map(int, input().split())

li = [[int(input()), False] for _ in range(n)]

nums = list(set(map(lambda x: x[0], li)))

result = []

for now in nums:
    for i in range(n):
        if li[i][0] == now:
            for j in range(1, k + 1):
                if i + j < n and li[i + j][0] == now:
                    li[i + j][1] = True
                    li[i][1] = True
    result.append([now, len(list(filter(lambda x: x[1], filter(lambda x: x[0] == now, li))))])

max_num = max(map(lambda x: x[1], result))
if max_num == 0:
    print(0)
    sys.exit()
for res in result:
    if res[1] == max_num:
        print(res[0])
        sys.exit()