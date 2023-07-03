import sys
import itertools


def num_baseball(s1, s2: str):
    strike = 0
    ball = 0
    for i in range(3):
        if int(s2[i]) in s1:
            if s1[i] == int(s2[i]):
                strike += 1
            else:
                ball += 1
    return str(strike), str(ball)


n = int(sys.stdin.readline())

li = []
for _ in range(n):
    li.append(list(sys.stdin.readline().rstrip().split()))

nums = [i for i in range(1, 10)]

permutation = list(itertools.permutations(nums, 3))

cnt = 0
for i in range(len(permutation)):
    flag = True
    for j in range(len(li)):
        strike, ball = num_baseball(permutation[i], li[j][0])
        if strike != li[j][1] or ball != li[j][2]:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)