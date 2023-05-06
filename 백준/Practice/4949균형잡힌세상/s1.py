import sys
import collections

class mystack:
    def __init__(self):
        self.stack_list = collections.deque()

    def push(self, item):
        self.stack_list.append(item)
    
    def pop(self):
        if len(self.stack_list) != 0:
            return self.stack_list.pop()
        else:
            return -1

    def size(self):
        return len(self.stack_list)

    def empty(self):
        if len(self.stack_list) == 0:
            return 1
        else:
            return 0
    
    def top(self):
        if len(self.stack_list) != 0:
            top = self.stack_list.pop()
            self.push(top)
            return top
        else:
            return -1

    def get(self):
        return self.stack_list

result = []
while True:
    stack = mystack()
    confirm_stack = mystack()
    s = input()
    if s == '.':
        break
    
    for i in range(len(s)):
        if s[i] == '[' or s[i] == ']' or s[i] == '(' or s[i] == ')':
            stack.push(s[i])
    
    while stack.size() != 0:
        tmp = stack.pop()
        if tmp == '[' and confirm_stack.top() == ']':
            confirm_stack.pop()
            continue
        if tmp == '(' and confirm_stack.top() == ')':
            confirm_stack.pop()
            continue
        confirm_stack.push(tmp)

    if confirm_stack.empty():
        result.append('yes')
    else:
        result.append('no')            
        
for i in range(len(result)):
    print(result[i])


