import collections
import sys

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

n = int(input())
queue = myqueue()
for i in range(n):
    s = sys.stdin.readline().split()
    if len(s) == 2:
        order = s[0]
        item = s[1]
    else:
        order = s[0]

    if order == 'push':
        queue.push(int(item))
    elif order == 'pop':
        print(queue.pop())
    elif order == 'size':
        print(queue.size())
    elif order == 'empty':
        print(queue.empty())
    elif order == 'front':
        print(queue.front())
    elif order == 'back':
        print(queue.back())