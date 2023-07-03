import sys
import collections

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())

    deq = collections.deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        if 'D' in p:
            print('error')
            continue
        else:
            print('[]')
            continue
    flag = False
    #true : head
    #false : tail
    head = True
    for i in range(len(p)):
        if p[i] == 'R':
            head = not head
        else:
            if len(deq) == 0:
                flag = True
                break
            else:
                if head:
                    deq.popleft()
                else:
                    deq.pop()
    if flag:
        print('error')
    else:
        print('[', end='')
        if not head:
            deq.reverse()
        print(','.join(deq), end='')
        print(']')
        