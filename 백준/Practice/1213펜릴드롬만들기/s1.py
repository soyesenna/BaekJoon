
import sys
import collections

s = sorted(list(sys.stdin.readline().rstrip()))

deq = collections.deque()

deq.extend(s)

if_odd = False
if len(deq) % 2 != 0:
    if_odd = True

i = 0
j = 1
flag = True
sol_num = -1
while True:
    if j == len(s) - 1:
        break
    if if_odd and j == len(s) - 2:
        sol_num = len(s) - 1
        break
    if s[i] != s[j]:
        if not if_odd:
            flag = False
            break
        else:
            if_odd = False
            sol_num = i
            i += 1
            j += 1
    else:
        i += 2
        j += 2

if flag:
    result_first = []
    result_last = []

    i = 0

    if sol_num == -1:
        for _ in range(len(s) // 2):
            result_first.append(s[i])
            result_last.append(s[i+1])
            i += 2
        for ch in result_first:
            print(ch, end='')
        for k in range(-1, -len(result_last)-1, -1):
            print(result_last[k], end='')
        print('')
    else:
        center = 0
        for _ in range(len(s) // 2 + 1):
            if i == sol_num:
                center = s[i]
                i += 1
            else:
                result_first.append(s[i])
                result_last.append(s[i+1])
                i += 2
        for ch in result_first:
            print(ch, end='')
        print(center, end='')
        for k in range(-1, -len(result_last)-1, -1):
            print(result_last[k], end='')
        print('')
else:
    print("I'm Sorry Hansoo")