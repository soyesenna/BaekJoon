

import sys
import itertools

n = int(sys.stdin.readline())

li = [1,5,10,50]

combination = list(itertools.combinations_with_replacement(li,n))

result = []
for nums in combination:
    sum_ = sum(nums)
    if sum_ not in result:
        result.append(sum_)

print(len(result))