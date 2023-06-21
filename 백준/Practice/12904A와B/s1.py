import sys
from copy import deepcopy

input = sys.stdin.readline


def solve(ori, tar):
    if ori == tar:
        return True
    elif len(ori) == len(tar):
        return False
    rev = deepcopy(ori)
    rev.reverse()
    rev.append("B")
    ori.append("A")
    return solve(deepcopy(ori), tar) or solve(rev, tar)


origin = list(input().rstrip())
target = list(input().rstrip())

if solve(origin, target):
    print(1)
else:
    print(0)