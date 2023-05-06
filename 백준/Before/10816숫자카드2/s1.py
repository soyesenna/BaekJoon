import sys
import collections

n = int(sys.stdin.readline())
num_list = sys.stdin.readline().split()

count = collections.Counter(num_list)

k = int(sys.stdin.readline())

k_list = sys.stdin.readline().split()

result = []
for i in range(k):
    if k_list[i] in count:
        result.append(count[k_list[i]])
    else:
        result.append(0)

s = ''
for i in range(len(result)):
    s += str(result[i]) + ' '

print(s[:-1])