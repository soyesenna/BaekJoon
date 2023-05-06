import sys
import collections

n, m = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))
li_deq = collections.deque(li)

deq = collections.deque([x for x in range(1, n+1)])

i = 0

total_cnt = 0
while i < len(li):
    left_ptr, left_cnt = 0, 0
    right_ptr, right_cnt = len(deq) - 1, 0
    right = False
    left = False
    while True:
        if deq[left_ptr] == li[i]:
            left = True
            break
        if deq[right_ptr] == li[i]:
            right = True
            break
        left_ptr += 1
        right_ptr -= 1
        right_cnt += 1
        left_cnt += 1
    if left:
        for _ in range(left_cnt):
            tmp = deq.popleft()
            deq.append(tmp)
        deq.popleft()
        total_cnt += left_cnt
    elif right:
        for _ in range(right_cnt):
            tmp = deq.pop()
            deq.appendleft(tmp)
        deq.pop()
        total_cnt += right_cnt + 1

    i += 1
    
print(total_cnt)