import sys
import collections

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

sort_li = sorted(li)
deq = collections.deque(li)

cnt = 0
while sort_li != list(deq):
    now = deq.popleft()
    tmp = collections.deque()
    if now == 1:
        max_ = sort_li[-1]
        while deq:
            a = deq.popleft()
            tmp.append(a)
            if a == max_:
                tmp.append(now)
        deq = tmp
    elif now == sort_li[-1]:
        deq.append(now)
    else:
        while deq:
            a = deq.popleft()
            if a == now + 1:
                tmp.append(now)
            tmp.append(a)
        deq = tmp
    cnt += 1
print(cnt)
