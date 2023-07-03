import sys

input = sys.stdin.readline


n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]

cups = [False, False, False]

result = 0
for i in range(3):
    cups[i] = True
    score = 0
    for now in li:
        cups[now[0] - 1], cups[now[1] - 1] = cups[now[1] - 1], cups[now[0] - 1]
        if cups[now[2] - 1]:
            score += 1
    result = max(result, score)
    cups[cups.index(True)] = False

print(result)
