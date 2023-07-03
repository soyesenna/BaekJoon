import queue
import sys
import collections

n = int(sys.stdin.readline())

w = 0
for _ in range(n):
    que = collections.deque()
    que.extend(sys.stdin.readline().rstrip())
    searched = []
    now = que.popleft()
    searched.append(now)
    before = now

    flag = True
    while que:
        now = que.popleft()
        if now not in searched:
            searched.append(now)
            before = now
        else:
            if before != now:
                flag = False
                break
    
    if flag:
        w += 1
print(w)

