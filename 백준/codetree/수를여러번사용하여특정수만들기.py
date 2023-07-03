import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

i = 0
result = 0
while i * a <= c:
    j = 0
    while True:
        now = (i * a) + (j * b)
        if now > c:
            break
        result = max(result, now)
        j += 1
    i += 1

print(result)