import sys

input = sys.stdin.readline

#사람수, 치즈수, 치즈를 먹은 기록수, 아픈기록수
n, m, d, s = map(int, input().split())

#[몇 번째 사람, 몇 번째 치즈, 언제 먹었는지]
eat_chart = [list(map(int, input().split())) for _ in range(d)]

#[몇 번째 사람, 언제 아팠는지]
sick_chart = [list(map(int, input().split())) for _ in range(s)]

sick_eat = [set() for _ in range(s)]
for i in range(len(sick_chart)):
    for j in range(d):
        if eat_chart[j][0] == sick_chart[i][0]:
            sick_eat[i-1].add(eat_chart[j][1])

sick_cheese = set()
for i in range(len(sick_eat)-1):
    sick_cheese = sick_eat[i] & sick_eat[i+1]

for cheese in list(sick_cheese):
    for i in range(d):
        if eat_chart[i][1] == cheese:


