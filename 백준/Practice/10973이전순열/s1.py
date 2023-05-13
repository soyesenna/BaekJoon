import sys
import itertools


n = int(sys.stdin.readline())
li = tuple(map(int, sys.stdin.readline().split()))

nums = [i for i in range(1, n + 1)]

permutation = list(itertools.permutations(nums, n))

idx = permutation.index(li)

if idx == 0:
    print(-1)
else:
    for num in permutation[idx - 1]:
        print(num, end=' ')