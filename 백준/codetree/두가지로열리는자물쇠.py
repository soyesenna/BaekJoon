import sys

input = sys.stdin.readline

n = int(input())

first = list(map(int, input().split()))
second = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            tmp = [i,j,k]
            flag = True
            for r in range(3):
                if 2 < abs(tmp[r] - first[r]) < n - 2:
                    flag = False
                    break
            if not flag:
                flag = True
                for r in range(3):
                    if 2 < abs(tmp[r] - second[r]) < n - 2:
                        flag = False
                        break
            if flag:
                cnt += 1

print(cnt)