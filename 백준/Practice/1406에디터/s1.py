import sys
import collections

s = sys.stdin.readline()
s_list = []
for i in range(len(s)):
    s_list.append(s[i])

s_list.pop()

n = int(sys.stdin.readline())

buff_deq = collections.deque()
for i in range(n):
    order = sys.stdin.readline().split()
    
    if order[0] == 'L':
        if len(s_list) != 0:
            buff_deq.appendleft(s_list.pop())
    elif order[0] == 'D':
        if len(buff_deq) != 0:
            s_list.append(buff_deq.popleft())
    elif order[0] == 'B':
        if len(s_list) != 0:
            s_list.pop()
    elif order[0] == 'P':
        s_list.append(order[1])

for i in range(len(buff_deq)):
    s_list.append(buff_deq.popleft())

print(''.join(s_list))