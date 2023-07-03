import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())

li = []
for _ in range(n):
    li.append(list(map(lambda x: [int(x), False], input().split())))

result = []

def dfs(r,c):
    global li,n,m,result

    stack = collections.deque()


