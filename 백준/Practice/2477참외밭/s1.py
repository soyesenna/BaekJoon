import sys
import collections

n = int(sys.stdin.readline())

cardinal = []
length = []
car_len = []

for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    cardinal.append(a)
    length.append(b)
    car_len.append([a,b])

length.extend(length)
cardinal.extend(cardinal)

max_horizon = max(car_len, key=lambda x: (x[0]==1 or x[0]==2, x[1]))
max_vertical = max(car_len, key=lambda x: (x[0]==3 or x[0]==4, x[1]))
result = max_horizon[1] * max_vertical[1]

before = None
for i in range(0, 12, 2):
    if before == None:
        before = [cardinal[i], cardinal[i + 1]]
        continue
    now = [cardinal[i], cardinal[i + 1]]
    if now == before:
        result -= length[i] * length[i - 1]
        break
    before = now

before = None
for i in range(1, 11, 2):
    if before == None:
        before = [cardinal[i], cardinal[i + 1]]
        continue
    now = [cardinal[i], cardinal[i + 1]]
    if now == before:
        result -= length[i] * length[i - 1]
        break
    before = now

print(result * n)