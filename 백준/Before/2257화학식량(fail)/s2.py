import sys
import collections

s = sys.stdin.readline().rstrip()

str_queue = collections.deque()

str_queue.extend(s)
#print(str_queue[0])

queue_stack = [collections.deque()]

result = 0

while len(str_queue) != 0:
    char = str_queue.popleft()
    int_to_push = 0

    if char == '(':
        tmp_queue = collections.deque()
        queue_stack.append(tmp_queue)
        continue
    elif char == ')':
        last_queue = queue_stack.pop()
        queue_sum = sum(last_queue)
        
        if len(str_queue) != 0:
            next_char = str_queue.popleft()
            if next_char >= '2' and next_char <= '9':
                queue_sum = queue_sum * int(next_char)
            else:
                str_queue.appendleft(next_char)
        result += queue_sum
    elif char >= '2' and char <= '9':
        tmp_int = queue_stack[-1][-1]
        int_to_push = tmp_int * (int(char) - 1)
        queue_stack[-1].append(int_to_push)
    else:
        if char == 'C':
            int_to_push = 12
        elif char == 'H':
            int_to_push = 1
        elif char == 'O':
            int_to_push = 16
    
        queue_stack[-1].append(int_to_push)

for i in range(len(queue_stack)):
    tmp_sum = sum(queue_stack.pop())
    result += tmp_sum
print(result)