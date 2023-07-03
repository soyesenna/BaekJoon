import sys

input = sys.stdin.readline

n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

time_li = [False for _ in range(1001)]

for time in times:
    for i in range(time[0], time[1]):
        time_li[i] = True

max_time = -1
for time in times:
    for i in range(time[0], time[1]):
        time_li = False
    a = len(list(filter(lambda x: x == True, time_li)))
    max_time = max(max_time, len(list(filter(lambda x: x == True, time_li))))
print(max_time)