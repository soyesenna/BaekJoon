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
            return True
        else:
            return False
    
    def top(self):
        if len(self.stack_list) != 0:
            top = self.stack_list.pop()
            self.push(top)
            return top
        else:
            return -1

k = int(input())

stack = mystack()

for i in range(k):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.push(n)

sum = 0
while not stack.empty():
    sum += stack.pop()

print(sum)

