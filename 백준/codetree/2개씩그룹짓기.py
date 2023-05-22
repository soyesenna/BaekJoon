import sys
import itertools

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

per = list(itertools.permutations([i for i in range(n)], 2))

res = []

for i in per:
    tmp = []