import sys
import collections

n = int(sys.stdin.readline())

result = []
for i in range(n):
    s = sys.stdin.readline().rstrip()
    deq = collections.deque()
    deq.extend(s)
    cursur = 0

    left_stack = collections.deque()
    right_queue = collections.deque()

    while len(deq) != 0:
        char = deq.popleft()

        if char == '<':
            if len(left_stack) != 0:
                a = left_stack.pop()
                right_queue.appendleft(a)
        elif char == '>':
            if len(right_queue) != 0:
                a = right_queue.popleft()
                left_stack.append(a)
        elif char == '-':
            if len(left_stack) != 0:
                left_stack.pop()
        else:
            left_stack.append(char)
    result.append(list(left_stack + right_queue))
for s in result:
    print(''.join(s))