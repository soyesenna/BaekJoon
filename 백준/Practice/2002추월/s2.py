import sys

n = int(sys.stdin.readline())

in_car = []

for i in range(n):
    in_car.append((i, sys.stdin.readline().rstrip()))

out_car = []
for i in range(n):
    out_car.append((i, sys.stdin.readline().rstrip()))

cnt = 0
for i in range(n):
    for j in range(n):
        if in_car[i][1] == out_car[j][1] and in_car[i][0] > out_car[j][0]:
            cnt += 1
            break
        elif in_car[i][1] == out_car[j][1] and in_car[i][0] <= out_car[j][0]:
            if in_car[i-1][1] != out_car[j-1][1]:
                cnt += 1
print(cnt)