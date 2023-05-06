import sys
import collections

n, k = map(int, sys.stdin.readline().split())

names = []
for i in range(n+k):
    s = sys.stdin.readline()
    names.append(s[:-1])

count = collections.Counter(names)

result_cnt = 0
result_name = []
for name in count:
    if count[name] == 2:
        result_cnt += 1
        result_name.append(name)
    
print(result_cnt)
result_name.sort()
for name in result_name:
    print(name)