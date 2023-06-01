import sys
import collections

input = sys.stdin.readline

n = int(input())

li = collections.deque(list(map(int, input().split())) for _ in range(n))

x_idx = list(map(lambda x: x[0], li))
y_idx = list(map(lambda x: x[1], li))

x_counter = collections.Counter(x_idx)
y_counter = collections.Counter(y_idx)

cnt = 0
for key in x_counter.keys():
    if x_counter[key] > 1:
        for _ in range(len(li)):
            now = li.popleft()
            if now[0] != key:
                li.append(now)
        cnt += 1
for key in y_counter.keys():
    if y_counter[key] > 1:
        flag = False
        for _ in range(len(li)):
            now = li.popleft()
            if now[1] != key:
                li.append(now)
            else:
                flag = True
        if flag:
            cnt += 1

print(len(li) + cnt)
if len(li) + cnt <= 3:
    print(1)
else:
    print(0)