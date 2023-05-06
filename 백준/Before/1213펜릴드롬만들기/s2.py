import sys
import collections

s = sorted(list(sys.stdin.readline().rstrip()))

result_first = []
result_last = []

deq = collections.deque()
deq.extend(s)

if_odd = False
if len(s) % 2 != 0:
    if_odd = True

odd_com = False
center = 0
flag = True

while deq:
    a = deq.popleft()
    try:
        b = deq.popleft()
    except:
        if if_odd and not odd_com:
            center = a
            odd_com = True
            break
    if a == b:
        result_first.append(a)
        result_last.append(b)
    else:
        if if_odd and not odd_com:
            center = a
            deq.appendleft(b)
            odd_com = True
        else:
            flag = False
            break

if flag:
    for i in range(len(result_first)):
        print(result_first[i], end='')
    if if_odd:
        print(center, end='')
    for i in range(-1, -len(result_last)-1, -1):
        print(result_last[i], end='')
    print('')
else:
    print("I'm Sorry Hansoo")
        