import sys
import collections

s = sys.stdin.readline()

stack = collections.deque()

for i in range(len(s)):
    stack.append(s[i])

stack.pop()
confirm_stack = collections.deque()

cnt = 0
before_open = False
while len(stack) != 0:
    tmp = stack.pop()
    if tmp == '(':
        if not before_open:
            cnt -= 1
            before_open = True
        else:
            cnt += 1
    else:
        cnt += 1
        before_open = False

print(cnt)
    