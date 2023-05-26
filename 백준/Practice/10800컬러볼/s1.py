import sys
from functools import reduce


input = sys.stdin.readline

n = int(input())

balls = [list(map(int, input().split())) for _ in range(n)]

#nlogn
#balls.sort(key=lambda x: x[1])

result = []

for ball in balls:
    result.append(reduce(lambda x, y: x + y[1], filter(lambda x: x[0] != ball[0] and x[1] < ball[1], balls), 0))

for res in result:
    sys.stdout.write(str(res) + '\n')

