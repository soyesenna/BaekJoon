import sys
import collections

input = sys.stdin.readline

#사람 수 , 치즈 수, 먹은 기록 수, 아픈 기록 수
n, m, d, s = map(int, input().split())

eat_chart = [list(map(int, input().split())) for _ in range(d)]
sick_chart = [list(map(int, input().split())) for _ in range(s)]

cheese = []
for sick in sick_chart:
    for eat in eat_chart:
        if eat[0] == sick[0] and eat[2] < sick[1]:
            cheese.append(eat[1])

counter = collections.Counter(cheese)
sick_cheese = list(set(filter(lambda x: counter[x] >= len(sick_chart), cheese)))
#print(sick_cheese)

if_sick = set()
for eat in eat_chart:
    if eat[1] in sick_cheese:
        if_sick.add(eat[0])

print(len(if_sick))
