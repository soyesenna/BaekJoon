import sys
import collections

input = sys.stdin.readline

#마을 수, 트럭 용량
n, c = map(int, input().split())
m = int(input())

li = [list(map(int, input().split())) for _ in range(m)]

li.sort(key=lambda x: (x[0], x[1], x[2]))
li = collections.deque(li)

delivery = 0
now_truck = collections.deque()
now_c = 0

for i in range(1, n+1):

    if len(now_truck) != 0:
        for _ in range(len(now_truck)):
            down = now_truck.popleft()
            if down[1] == i:
                delivery += down[2]
                now_c -= down[2]
            else:
                now_truck.append(down)

    for _ in range(len(li)):
        up = li.popleft()
        if up[0] == i:
            now_c += up[2]
            if now_c > c:
                over = now_c - c
                now_c -= over
                up[2] -= over
            now_truck.append(up)
        else:
            li.append(up)

print(delivery)

