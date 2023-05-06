import sys

c = int(sys.stdin.readline())

result = []
for _ in range(c):
    li = list(map(int, sys.stdin.readline().split()))

    sum = 0
    for i in range(1, li[0]+1):
        sum += li[i]
    avg = sum / li[0]

    over = 0
    for i in range(1, li[0]+1):
        if li[i] > avg:
            over += 1
    
    result.append(round((over/li[0]) * 100, 3))

for res in result:
    print("{:.3f}%".format(res))
    