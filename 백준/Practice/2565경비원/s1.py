from posixpath import split
import sys
import collections

def clock(root, store):
    cardinals = collections.deque([1,4,2,3])
    for _ in range(4):    
        now = cardinals.popleft()
        if now == store[0]:
            cardinals.appendleft(now)
            break
        cardinals.append(now)
    


input = sys.stdin.readline

#가로, 세로
n, m = map(int, input().split())
t = int(input())

#cardinal, num, left, right
#cardinal, num, up, down
stores = collections.deque()
for _ in range(t):
    cardinal, num = map(int, input().split())
    if cardinal == 1 or cardinal == 2:
        stores.append([cardinal, num, num, n - num])
    else:
        stores.append([cardinal, num, num, m - num])

root = list(map(int, input().split()))

