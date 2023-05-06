import sys
import collections
from unittest import result

deq = collections.deque(sys.stdin.readline().rstrip())

result_deq = collections.deque()

reverse = True
tmp_list = []
while len(deq) != 0:
    char = deq.popleft()

    if char == '<':
        if len(tmp_list) != 0:
            tmp_list.reverse()
            result_deq.extend(tmp_list)
            tmp_list = []
        tmp_list.append(char)
        reverse = False
    elif char == '>':
        reverse = True
        tmp_list.append(char)
        result_deq.extend(tmp_list)
        tmp_list = []
    elif (char == ' ' and reverse):
        
        tmp_list.reverse()
        tmp_list.append(char)
        result_deq.extend(tmp_list)
        tmp_list = []
    elif len(deq) == 0 and len(tmp_list) != 0:
        tmp_list.append(char)
        #tmp_list.append(' ')
        tmp_list.reverse()
        #tmp_list.pop()
        result_deq.extend(tmp_list)
    else:
        tmp_list.append(char)
        
for i in result_deq:
    print(i, end='')
