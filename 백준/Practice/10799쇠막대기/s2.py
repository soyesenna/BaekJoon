import sys
import collections

s = sys.stdin.readline()

stack = collections.deque()

for i in range(len(s)):
    stack.append(s[i])

stack.pop()
confirm_stack = collections.deque()

cnt = 0
while len(stack) != 0:
    tmp = stack.pop()
    if tmp == '(':
        confirm_stack.pop()
        cnt += len(confirm_stack)
        
        while True:
            if len(stack) != 0:
                tmp2 = stack.pop()
                if tmp2 == '(':
                    cnt += 1
                    confirm_stack.pop()
                else:
                    stack.append(tmp2)
                    break
            else:
                break
    else:
        confirm_stack.append(tmp)

print(cnt)