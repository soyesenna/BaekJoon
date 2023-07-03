import sys
import collections

n, k = map(int, sys.stdin.readline().split())

num_list = [i for i in range(1, n+1)]

deq = collections.deque()
deq.extend(num_list)

step = k-1
result = []

while deq:
    for _ in range(step):
        a = deq.popleft()
        deq.append(a)
    result.append(deq.popleft())
   
print('<', end='')
for i in range(len(result)-1):
    print(result[i], end=', ')
print(str(result[-1])+'>')
