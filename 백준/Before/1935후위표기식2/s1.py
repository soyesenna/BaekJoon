import sys
import collections

n = int(sys.stdin.readline())

s = sys.stdin.readline().rstrip()

alpha_num = {}
ascii = 65
for i in range(n):
    tmp = int(sys.stdin.readline())
    alpha_num[chr(ascii)] = tmp
    ascii += 1

result = 0.0

stack = collections.deque()

for i in range(len(s)):
    if s[i] in alpha_num:
        stack.append(alpha_num[s[i]])
    else:
        a = stack.pop()
        b = stack.pop()
        if s[i] == '*':
            stack.append(b*a)
        elif s[i] == '/':
            stack.append(b/a)
        elif s[i] == '+':
            stack.append(b+a)
        elif s[i] == '-':
            stack.append(b-a)

print('%.2f'%stack[0])