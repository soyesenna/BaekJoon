import sys
import collections

n = int(sys.stdin.readline())

first = collections.Counter(list(sys.stdin.readline().rstrip()))

cnt = 0
for _ in range(n-1):
    now = collections.Counter(list(sys.stdin.readline().rstrip()))

    diff_count = 1
    flag = True
    for key in now.keys():
        if key not in first.keys():
            if now[key] > 1:
                flag = False
                break
            else:
                if diff_count == 1:
                    diff_count -= 1
                else:
                    flag = False
                    break
        else:
            if abs(first[key] - now[key]) == 1:
                if diff_count == 1:
                    diff_count -= 1
                else:
                    flag = False
                    break
            elif abs(first[key] - now[key]) > 1:
                flag = False
                break
    if flag:
        cnt += 1

print(cnt)