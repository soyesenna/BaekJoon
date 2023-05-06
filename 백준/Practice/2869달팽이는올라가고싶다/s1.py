import sys

a, b, v = map(int, sys.stdin.readline().split())

day_up = a - b

now = (v // day_up - (a + 1)) * day_up
now_day = v // day_up - (a + 1)
while True:
    now += a
    now_day += 1
    if now >= v:
        break
    now -= b

print(now_day)
