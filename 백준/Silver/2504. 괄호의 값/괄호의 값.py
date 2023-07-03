import sys
import collections

s = sys.stdin.readline().rstrip()
queue = collections.deque(s)

li = []
nums = []

while queue:
    now = queue.popleft()
    li.append(now)
    if len(li) <= 1:
        continue
    if li[-1] == ')':
        if li[-2] == '(':
            li.pop()
            li.pop()
            li.append(2)
        elif type(li[-2]) == int and len(li) > 2 and li[-3] == '(':
            li.pop()
            a = li.pop()
            li.pop()
            li.append(2 * a)
    elif li[-1] == ']':
        if li[-2] == '[':
            li.pop()
            li.pop()
            li.append(3)
        elif type(li[-2]) == int and len(li) > 2 and li[-3] == '[':
            li.pop()
            a = li.pop()
            li.pop()
            li.append(3 * a)
    
    for i in range(len(li) - 1):
        if type(li[i]) == int and type(li[i + 1]) == int:
            a = li.pop()
            b = li.pop()
            li.append(a+b)

tmp = ['(', ')', '[', ']']
for i in tmp:
    if i in li:
        print(0)
        sys.exit()
print(li[0])
