import sys
import collections

t = int(sys.stdin.readline())
result_list = []

for i in range(t):
    n = int(sys.stdin.readline())

    fassions = []
    for j in range(n):
        s = list(sys.stdin.readline().split())
        fassions.append(s[1])
    count = collections.Counter(fassions)
    val_list = list(count.values())
    result = 1
    for k in range(len(val_list)):
        result = result * (val_list[k] + 1)
    result -= 1
    result_list.append(result)

for i in result_list:
    print(i)