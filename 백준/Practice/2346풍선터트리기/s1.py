import sys
import collections

n = int(sys.stdin.readline())

my_deque = collections.deque(enumerate(((list(map(int, sys.stdin.readline().split()))))))
result_list = []
idx = 0
for i in range(n-1):
    now = my_deque.popleft()
    result_list.append(now[0])
    if now[1] < 0:
        idx = abs(now[1]) % len(my_deque)
        for j in range(idx-1):
            tmp = my_deque.pop()
            my_deque.appendleft(tmp)
    elif now[1] > 0:
        idx = now[1] % len(my_deque)
        for j in range(idx-1):
            tmp = my_deque.popleft()
            my_deque.append(tmp)

result_list.append(my_deque.pop())
for i in range(len(result_list)):
    print(result_list[i][0]+1, end=' ')
#print('\n')