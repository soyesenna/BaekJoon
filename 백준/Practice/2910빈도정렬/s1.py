import sys
import collections

n, c = map(int, sys.stdin.readline().split())

count = collections.Counter(list(map(int, sys.stdin.readline().split())))


for value, idx in count.most_common(n):
    for i in range(idx):
        print(value, end=' ')
    
