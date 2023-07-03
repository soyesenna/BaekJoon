import sys
from functools import reduce

input = sys.stdin.readline

n, k = map(int, input().split())

dia = [list(map(int, input().split())) for _ in range(n)]

bag = [int(input()) for _ in range(k)]


def check(x):
    global bag
    min_bag = min(bag)
    if x[0] <= min_bag:
        return True
    return False


fit = list(filter(lambda x: check(x), dia))
fit.sort(key=lambda x: -x[1])

result = reduce(lambda x, y: x+y, map(lambda x: x[1], fit), 0)
print(result)