import sys
import collections

def log(n):
    cnt = 0
    while n > 1:
        n //= 2
        cnt += 1
    return cnt

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
result = [0 for _ in range(63)]

counter = collections.Counter(li)

counter = sorted(list(counter.items()), key=lambda x: x[0])
for i in range(len(counter)):
    if counter[i][0] == 0:
        continue
    result[log(counter[i][0])] = counter[i][1]

for i in range(len(result) - 1):
    result[i + 1] += result[i] // 2

for i in range(len(result) - 1, -1, -1):
    if result[i] != 0:
        print(2 ** i)
        sys.exit()

