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
            return True
        else:
            return False

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


n = int(input())

stack = mystack()
num_queue = myqueue()

for i in range(n):
    tmp = int(sys.stdin.readline())
    num_queue.push(tmp)

i = 1
result = []
FLAG = True
while True:
    if stack.top() == num_queue.front() and not num_queue.empty():
        stack.pop()
        result.append('-')
        num_queue.pop()
        continue
    if i > n:
        if num_queue.empty():
            break
        else:
            FLAG = False
            break
    stack.push(i)
    result.append('+')
    i += 1

if FLAG:
    for i in range(len(result)):
        print(result[i])
else:
    print('NO')

