import sys
import collections

input = sys.stdin.readline

n, m, h, k = map(int, input().split())

orders = collections.deque(input().rstrip())

healths = [list(map(int, input().split())) for _ in range(m)]

now = [0,0]
get_health = []
while orders:
    order = orders.popleft()
    if order == 'R':
        now[0] += 1
    elif order == 'L':
        now[0] -= 1
    elif order == 'U':
        now[1] += 1
    else:
        now[1] -= 1

    h -= 1
    if h < 0:
        print("No")
        sys.exit()
    if h < k and (now not in get_health) and (now in healths):
        h = k
        get_health.append(now)

if h < 0:
    print("No")
else:
    print("Yes")