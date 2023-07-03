import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dia = [list(map(int, input().split())) for _ in range(n)]

bag = [int(input()) for _ in range(k)]

dia.sort(key=lambda x: (-x[1]))
bag.sort()

result = 0
bag_size = k
for i in range(n):
    if bag_size == 0:
        print(result)
        sys.exit()
    for j in range(len(bag)):
        if bag[j] >= dia[i][0]:
            result += dia[i][1]
            bag[j] = 0
            bag_size -= 1
            break

print(result)