import sys
import itertools
from cProfile import Profile
from pstats import Stats

profile = Profile()

def main():
    n = int(sys.stdin.readline())

    li = tuple(map(int, sys.stdin.readline().split()))
    li = tuple([i for i in range(1, 101)])

    nums = [i for i in range(1, n + 1)]

    per1 = list(itertools.permutations(nums, n - 1))
    #per2 = list(itertools.permutations(nums, n - 1))

    print(li[1:])
    print(per1[0])
    if li[1:] == per1[0]:
        print(str(li[0] - 1) + ''.join(per1[-1]))
    else:
        print(str(li[0]) + ''.join(per1[per1.index(li[1:]) - 1]))


profile.run("main()")
stats = Stats(profile)
stats.print_stats()