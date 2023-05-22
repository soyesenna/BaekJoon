import sys
import collections

n, w, l = map(int, sys.stdin.readline().split())

trucks = collections.deque(map(int, sys.stdin.readline().split()))

now_bridge = collections.deque([0 for _ in range(w)])
cnt = 0
while trucks:
    now_bridge.popleft()
    if sum(now_bridge) > l:
        cnt += 1
        now_bridge.append(0)
        continue
    else:
        now_truck = trucks.popleft()
        if sum(now_bridge) + now_truck > l:
            now_bridge.append(0)
            trucks.appendleft(now_truck)
            cnt += 1
            continue
        else:
            cnt += 1
            now_bridge.append(now_truck)

print(cnt + w)