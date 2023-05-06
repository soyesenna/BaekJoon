import collections
import sys

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

n = int(input())
stack = mystack()
for i in range(n):
    s = sys.stdin.readline().split()
    if len(s) == 2:
        order = s[0]
        item = s[1]
    else:
        order = s[0]

    if order == 'push':
        stack.push(int(item))
    elif order == 'pop':
        print(stack.pop())
    elif order == 'size':
        print(stack.size())
    elif order == 'empty':
        print(stack.empty())
    elif order == 'top':
        print(stack.top())