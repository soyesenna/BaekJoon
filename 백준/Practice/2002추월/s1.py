import sys

n = int(sys.stdin.readline())

in_car = []
for i in range(n):
    if i == 0:
        in_car.append((None, sys.stdin.readline().rstrip()))
        continue
    in_car.append((in_car[-1][1], sys.stdin.readline().rstrip()))

out_car = []
for i in range(n):
    if i == 0:
        out_car.append((None, sys.stdin.readline().rstrip()))
        continue
    out_car.append((out_car[-1][1], sys.stdin.readline().rstrip()))

print(in_car, out_car)
cnt = 0
for i in range(n):
    for j in range(n):
        if in_car[i][1] == out_car[j][1]:
            if in_car[i][0] != out_car[j][0] and in_car[i][0] != None:
                cnt += 1
print(cnt)