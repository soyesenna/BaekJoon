import sys
import collections

n = int(sys.stdin.readline())

first = sorted(list(sys.stdin.readline().rstrip()))
first_deq = collections.deque()
first_deq.extend(first)
first_len = len(first)

cnt = 0
for _ in range(n-1):
    now = sorted(list(sys.stdin.readline().rstrip()))
    #now_count = collections.Counter(now)
    now_deq = collections.deque()
    now_deq.extend(now)
    now_len = len(now)

    flag = True
    if now_len - first_len == 1:
        diff = False
        for i in range(first_len):
            a = now_deq.popleft()
            if a != first[i]:
                if not diff:
                    diff = True
                else:
                    flag = False
                    break
    elif now_len - first_len == -1:
        diff = False
        
        for i in range(now_len):
            a = first_deq.popleft()
            if a != now[i]:
                if not diff:
                    diff = True
                else:
                    flag = False
                    break
        first_deq.extend(first)
    elif now_len - first_len == 0:
        diff = False

        for i in range(first_len):
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