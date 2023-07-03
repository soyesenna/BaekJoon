import sys
import collections

input = sys.stdin.readline

x, y = map(int, input().split())

cnt = 0
for i in range(x, y + 1):
    deq = collections.deque(str(i))
    while deq:
        if len(deq) == 1:
            break
        left = deq.popleft()
        right = deq.pop()
        if left != right:
            cnt -= 1
            break
    cnt += 1
print(cnt)