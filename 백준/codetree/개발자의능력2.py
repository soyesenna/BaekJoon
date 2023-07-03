import sys

input = sys.stdin.readline

li = list(map(int, input().split()))

li.sort()

res = [li[-1] + li[0], li[-2] + li[1], li[-3] + li[2]]
max_team = max(res)
min_team = min(res)

print(max_team - min_team)