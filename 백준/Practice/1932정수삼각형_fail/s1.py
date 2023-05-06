import sys
import collections

        
n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)

