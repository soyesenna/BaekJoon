import sys
import itertools


num = (list(map(int, sys.stdin.readline().split())))
nums = []
for i in range(len(num)):
    tmp = []
    for j in range(i, i + 4):
        if j > 3:
            j %= 4
        tmp.append(num[j])
    nums.append(tuple(tmp))
num = min(nums)

li = [i for i in range(1, 10)]

pro = list(itertools.product(li, li, li, li))

num_set = set()
for i in range(len(com)):
    for k in range(len(com[i])):
        tmp = []
        for j in range(k, k + 4):
            if j > 3:
                j %= 4
            tmp.append(com[i][j])
        num_set.add(tuple(tmp))

num_li = sorted(list(num_set))
print(num_li)
print(num_li.index(num) + 1)

