import sys

n = int(sys.stdin.readline())

days = [tuple(sys.stdin.readline().split()) for _ in range(n)]

days_rain = list(filter(lambda x: (x[2] == "Rain"), days))

day = list(map(lambda x: tuple(x[0].split('-')), days_rain))

day.sort(key=lambda x: (x[0], x[1], x[2]))
day_result = ''
for i in range(3):
    day_result += str(day[0][i]) + '-'

day_result = day_result[:-1]
for res in days:
    if res[0] == day_result:
        print(res[0], res[1], res[2])

