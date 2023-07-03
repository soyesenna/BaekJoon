import sys

input = sys.stdin.readline

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

time_li = [0 for _ in range(1001)]

for time in times:
    for i in range(time[0], time[1]):
        time_li[i] += 1

max_time = -1
for time in times:
    for i in range(time[0], time[1]):
        time_li[i] -= 1
    max_time = max(max_time, len(list(filter(lambda x: x > 0, time_li))))
    for i in range(time[0], time[1]):
        time_li[i] += 1
print(max_time)