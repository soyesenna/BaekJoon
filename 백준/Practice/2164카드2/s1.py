import collections
import sys

n = int(sys.stdin.readline())
mydeque = collections.deque()

for i in range(1, n+1):
    mydeque.append(i)

while len(mydeque) != 1:
    mydeque.popleft()
    a = mydeque.popleft()
    mydeque.append(a)

print(mydeque.pop())