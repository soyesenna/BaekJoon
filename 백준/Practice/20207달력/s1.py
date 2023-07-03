import sys

input = sys.stdin.readline

n = int(input())

days = [list(map(int, input().split())) for _ in range(n)]
days.sort(key=lambda x: (x[0], -x[1]))

calendar_ = [[0 for _ in range(366)] for _ in range(n)]

for day in days:
    for i in range(n):
        if sum(calendar_[i][day[0]:day[1]+1]) == 0:
            for j in range(day[0], day[1]+1):
                calendar_[i][j] = 1
            break



rotate = [list(e) for e in zip(*calendar_[::-1])]

flag = False
rect = []
for i in range(len(rotate)):
    if sum(rotate[i]) != 0:
        if not flag:
            rect.append(i)
            flag = True
    else:
        if flag:
            rect.append(i)
            flag = False

if len(rect) % 2 != 0:
    rect.append(366)

result = []

min_c = 100
while rect:
    b = rect.pop()
    a = rect.pop()

    for i in range(a, b):
        min_c = min(min_c, rotate[i].index(1))
    result.append((b - a) * (n - min_c))

print(sum(result))