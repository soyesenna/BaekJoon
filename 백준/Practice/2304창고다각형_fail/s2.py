import sys
import collections

n = int(sys.stdin.readline())

li = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    li.append(tmp)

max_index = max(li, key=lambda x: x[1])[0]
deq = collections.deque(sorted(li, key=lambda x : x[0]))

left_max = deq.popleft()
right_max = deq.pop()

result = 0
left_done = False
right_done = False
if left_max[0] == max_index:
    left_done = True
if right_max[0] == max_index:
    right_done = True
while (not left_done) or (not right_done):
    if not left_done:
        left = deq.popleft()
        
        if left[0] == max_index:
            left_done = True
            result += left_max[1] * (left[0] - left_max[0])
            deq.appendleft(left)
        elif left_max[1] < left[1]:
            result += left_max[1] * (left[0] - left_max[0])
            left_max = left
        
    if not right_done:
        right = deq.pop()
        
        if right[0] == max_index:
            right_done = True
            result += right_max[1] * (right_max[0] - right[0])
            deq.append(right)
        elif right_max[1] < right[1]:
            result += right_max[1] * (right_max[0] - right[0])
            right_max = right

if len(deq) != 0:
    if len(deq) == 1:
        a = deq.popleft()
        result += a[1]
    else:
        a = deq.popleft()
        b = deq.pop()
        result += a[1] * (b[0] - a[0] + 1)
print(result)