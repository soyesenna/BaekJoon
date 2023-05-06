from itertools import count
import sys
import collections

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num = int(sys.stdin.readline())

    num_list.append(num)

num_list.sort()
counter = collections.Counter(num_list)
count_list = []
for key in counter:
    tmp = []
    tmp.append(key)
    tmp.append(counter[key])
    count_list.append(tmp)

count_list.sort(key=lambda x:-x[1])

#print(count_list)
avg = sum(num_list) / n
s = "%.0f"%avg
if s == '-0':
    print(-int(s))
else:
    print(int(s))

print(num_list[n//2])

if len(count_list) >= 2:
    if count_list[0][1] == count_list[1][1]:
        print(count_list[1][0])
    else:
        print(count_list[0][0])
else:
    print(count_list[0][0])

print(num_list[-1] - num_list[0])
