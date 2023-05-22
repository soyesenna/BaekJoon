import sys

li = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]

for i in range(len(li)):
    before = li[i][0]
    cnt = 1
    for j in range(1, 19):
        if before != li[i][j]:
            if cnt == 5:
                print(before)
                print(i+1, j - 4)
                sys.exit()
            else:
                cnt = 1
        else:
            cnt += 1
        before = li[i][j]

for i in range(len(li)):
    before = li[0][i]
    cnt = 1
    for j in range(1, 19):
        if before != li[j][i]:
            if cnt == 5:
                print(li[j-1][i])
                print(j - 4, i+1)
                sys.exit()
            else:
                cnt = 1
        else:
            cnt += 1
        before = li[j][i]

for k in range(len(li) - 4):
    i = k
    j = 0
    before = li[i][j]
    cnt = 1
    while i + 1 < 19 and j + 1 < 19:
        if before != li[i+1][j+1]:
            if cnt == 5:
                print(li[i][j])
                print(i-3,j-3)
                sys.exit()
            else:
                cnt = 1
        else:
            cnt += 1
        before = li[i+1][j+1]
        i += 1
        j += 1


for k in range(len(li) - 4):
    i = k
    j = 0
    before = li[j][i]
    cnt = 1
    while i - 1 > 0 and j + 1 < 19:
        if before != li[j+1][i-1]:
            if cnt == 5:
                print(li[j-1][i+1])
                print(j-3,i+3)
                sys.exit()
            else:
                cnt = 1
        else:
            cnt += 1
        before = li[j+1][i-1]
        i -= 1
        j += 1
    if cnt == 5:
        print(li[j-2][i+2])
        print(i+4,j-3)
        sys.exit()


print(0)