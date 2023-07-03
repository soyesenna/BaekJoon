import sys

input = sys.stdin.readline

li = list(map(int, input().split()))
total_sum = sum(li)

result = 3e10+10

for i in range(5):
    now_one = li[i]
    extra = li[:i] + li[i+1:]
    for j in range(4):
        for k in range(j + 1, 4):
            extra_one = extra[j] + extra[k]
            extra_two = total_sum - extra_one - now_one
            max_team = max([now_one, extra_one, extra_two])
            min_team = min([now_one, extra_one, extra_two])

            if now_one != extra_one and now_one != extra_two and extra_one != extra_two:
                result = min(result, max_team - min_team)

if result != 3e10+10:
    print(result)
else:
    print(-1)