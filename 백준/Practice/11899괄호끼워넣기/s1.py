import sys
import collections

s = list(sys.stdin.readline().rstrip())

deq_stack = collections.deque(s)
deq_queue = collections.deque()

for _ in range(len(deq_stack)):
    a = deq_stack.pop()
    if a == '(':
        if len(deq_queue) != 0:
            b = deq_queue.popleft()
            if b == ')':
                pass
            else:
                deq_queue.appendleft(a)
                deq_queue.appendleft(b)
        else:
            deq_queue.appendleft(a)
    else:
        deq_queue.appendleft(a)


print(len(deq_queue))
