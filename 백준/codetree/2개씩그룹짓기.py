import sys
import itertools

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

com = list(itertools.combinations(li, 2))

sum_res = list(map(lambda x: x[0] + x[1], com))
print(sum_res)
sum_res.remove(max(sum_res))
print(max(sum_res))