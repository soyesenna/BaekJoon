import sys
import itertools

input = sys.stdin.readline

n = int(input())

li = [list(input().split()) for _ in range(n)]

per = list(itertools.permutations([i for i in range(1, 10)], 3))

cnt = 0
for p in per:
    flag = False
    for i in range(n):
        now = [0, 0]
        for j in range(3):
            if int(li[i][0][j]) in p:
                if p.index(int(li[i][0][j])) == j:
                    now[0] += 1
                else:
                    now[1] +=1
        if now[0] == int(li[i][1]) and now[1] == int(li[i][2]):
            flag = True
        else:
            flag = False
            break
    if flag:
        cnt += 1

print(cnt)
