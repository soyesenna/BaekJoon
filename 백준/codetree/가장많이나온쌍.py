import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())

li = [tuple(sorted(list(map(int, input().split())))) for _ in range(m)]

counter = collections.Counter(li)

print(max(counter.values()))