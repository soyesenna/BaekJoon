import sys

t = int(sys.stdin.readline())

result = []
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    seat = [i for i in range(m)]

    li = list(map(int, sys.stdin.readline().split()))

    for now in li:
        if now == -1:
            if 'n' not in seat:
                seat[-1] = 'n'
                continue
            can = seat.index('n') - 1
            if can >= 0:
                if seat[can] != 'n':
                    seat[can] = 'n'
                else:
                    n -= 1
        elif now == -2:
            if 'n' not in seat:
                seat[0] = 'n'
                continue
            for i in range(m -1, -1, -1):
                if seat[i] == 'n':
                    can = i + 1
                    break
            if can == m:
                n -= 1
                continue
            if can <= m - 1:
                if seat[can] != 'n':
                    seat[can] = 'n'
        else:
            if seat[now - 1] == 'n':
                n -= 1
            else:
                seat[now - 1] = 'n'

    result.append(n)

print(result)