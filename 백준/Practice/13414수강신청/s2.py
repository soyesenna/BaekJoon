import sys
import collections

k, l = map(int, sys.stdin.readline().split())

deq_set = dict()

for i in range(l):
    deq_set[(sys.stdin.readline().rstrip())] = i

#print(deq_set)
#print(sorted(deq_set, key=deq_set.__getitem__))
i = 0
for key in sorted(deq_set, key=deq_set.__getitem__):
    if i == k:
        break
    print(key)
    i += 1