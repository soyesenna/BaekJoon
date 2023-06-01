import sys
import collections

input = sys.stdin.readline

li = [input().rstrip() for _ in range(3)]

result = set()
for i in range(3):
    counter = collections.Counter(li[i])
    if len(counter.keys()) == 2:
        result.add(tuple(counter.keys()))
for i in range(3):
    counter = collections.Counter(map(lambda x: x[i], li))
    if len(counter.keys()) == 2:
        result.add(tuple(counter.keys()))
tmp = []
for i in range(3):
    tmp.append(li[i][i])
counter = collections.Counter(tmp)
if len(counter.keys()) == 2:
    result.add(tuple(counter.keys()))

tmp = []
for i in range(2, -1, -1):
    tmp.append(li[2-i][i])
counter = collections.Counter(tmp)
if len(counter.keys()) == 2:
    result.add(tuple(counter.keys()))
print(len(result))
