n = int(input())

res = 0
for i in range(2, 6 + 2):
    d = i + 5
    j = 1
    while True:
        now = i + (d * j)
        if now > n:
            break
        elif now == n:
            res = j + 2
            break
        j += 1

print(res)
