import sys
import collections

k, l = map(int, sys.stdin.readline().split())

deq_stack = collections.deque()

for i in range(l):
    deq_stack.append((sys.stdin.readline().rstrip()))

result_deq = collections.deque()
#print(deq_stack)
for _ in range(len(deq_stack)):
    a = deq_stack.pop()
    if a in result_deq:
        a = 'n' + a
    result_deq.appendleft(a)

#print(result_deq)
i = 0
for _ in range(len(result_deq)):
    if i == k:
        break
    a = result_deq.popleft()
    if a[0] != 'n':
        print(a)
        i += 1