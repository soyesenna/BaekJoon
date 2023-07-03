import sys

input = sys.stdin.readline

n = int(input())

days = [list(map(int, input().split())) for _ in range(n)]

calendar_ = [0 for _ in range(366)]

for day in days:
    for i in range(day[0], day[1]+1):
        calendar_[i] += 1

c = ''.join(map(lambda x: str(x), calendar_)).removeprefix('0').removesuffix('0')

calendar_ = c.split('0')

result = []
for i in range(len(calendar_)):
    if calendar_[i] != '':
        max_ = max(calendar_[i], key=lambda x: int(x))
        result.append(len(calendar_[i]) * int(max_))

print(sum(result))