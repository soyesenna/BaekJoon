import sys
import itertools

n = int(sys.stdin.readline())
li = tuple(map(int, sys.stdin.readline().split()))

if li[0] == 1:
    nums = [i for i in range(li[0] * len(li), n + 1)]

print(nums)
permutation = list(itertools.permutations(nums, n))
print(permutation)
idx = permutation.index(li)

if idx == 0:
    print(-1)
else:
    for num in permutation[idx - 1]:
        print(num, end=' ')