import sys
import collections

n = int(sys.stdin.readline())

first = list(sys.stdin.readline().rstrip())

cnt = 0
for _ in range(n-1):
    now = list(sys.stdin.readline().rstrip())

    diff_count = 0
    flag = True
    if abs(len(now) - len(first)) > 1:
        flag = False
    elif (len(now) - len(first)) == 1:
        for i in range(len(first)):
            if first[i] not in now:
                flag = False
                break
            del now[now.index(first[i])]
    elif len(now) - len(first) == -1:
        for i in range(len(now)):
            if first[i] not in now:
                flag = False
                break
            del now[now.index(first[i])]
    else:
        for i in range(len(first)):
            if first[i] not in now:
                if diff_count == 0:
                    diff_count += 1
                else:
                    flag = False
                    break
            else:
                del now[now.index(first[i])]
        if diff_count == 0 and len(now) > 1:
            flag = False
    if flag:
        cnt += 1

print(cnt)