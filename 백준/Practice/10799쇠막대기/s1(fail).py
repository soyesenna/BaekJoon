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

class myqueue:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if len(self.queue) != 0:
            return self.queue.popleft()
        else:
            return -1
    
    def size(self):
        return len(self.queue)

    def empty(self):
        if len(self.queue) == 0:
            return 1
        else:
            return 0

    def front(self):
        if len(self.queue) != 0:
            item = self.queue.popleft()
            self.queue.appendleft(item)
            return item
        else:
            return -1

    def back(self):
        if len(self.queue) != 0:
            item = self.queue.pop()
            self.queue.append(item)
            return item
        else:
            return -1

s = sys.stdin.readline()

stack = collections.deque()

for i in range(len(s)):
    stack.append(s[i])

stack.pop()
confirm_stack = collections.deque()




laser = 0
cnt = 0
while len(stack) != 0:
    if len(confirm_stack) == 0:
        laser = 0
    tmp = stack.pop()
    if tmp == '(':
        confirm_stack.pop()

        laser += 1
        if len(confirm_stack) == 0 and len(stack) == 0:
            break
        tmp2 = stack.pop()

        
        if tmp2 == '(':
            cnt += laser + 1
            confirm_stack.pop()
        else:
            stack.append(tmp2)
    else:
        confirm_stack.append(tmp)

print(cnt)
