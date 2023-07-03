import sys
import itertools

def get_clock(num):
    nums = []
    for i in range(len(num)):
        tmp = []
        for j in range(i, i + 4):
            if j > 3:
                j %= 4
            tmp.append(num[j])
        nums.append(tuple(tmp))
    num = min(nums)
    return num

num = (list(map(int, sys.stdin.readline().split())))
input_clock = get_clock(num)
#print(input_clock)

li = [i for i in range(1, 10)]

pro = list(itertools.product(li, li, li, li))

clocks = set()
for i in range(len(pro)):
    clocks.add(get_clock(pro[i]))
#print(clocks)
clocks = sorted(list(clocks))
print(clocks.index(input_clock) + 1)