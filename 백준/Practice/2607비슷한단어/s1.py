import sys
import collections

n = int(sys.stdin.readline())

first = sorted(list(sys.stdin.readline().rstrip()))

cnt = 0
for _ in range(n-1):
    now = sorted(list(sys.stdin.readline().rstrip()))
    flag = True

    len_diff = len(first) - len(now)
    if len_diff == 1:
        i = 0
        j = 0
        for _ in range(len(now)):
            if first[i] != now[j]:
                flag = False
                break
    elif len_diff == -1:
        for i in range(len(first)):
            if first[i] != now[i]:
                flag = False
                break
    elif len_diff == 0:
        diff = False
        for i in range(len(first)):
            if first[i] != now[i]:
                if not diff:
                    diff = True
                else:
                    flag = False
                    break
    else:
        flag = False
    
    if flag:
        cnt += 1

print(cnt)