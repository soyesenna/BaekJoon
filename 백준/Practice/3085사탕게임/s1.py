import sys
import collections

n = int(sys.stdin.readline())
result = []

def count_candy(candies):
    global n
    global result


    for i in range(n):
        queue = collections.deque(candies[i])
        before = ''
        cnt = 1
        for j in range(n):
            if before == '':
                before = queue.popleft()
            else:
                now = queue.popleft()
                if now == before:
                    cnt += 1
                    if cnt == n:
                        print(cnt)
                        sys.exit()
                else:
                    result.append(cnt)
                    cnt = 1
                    before = now
        result.append(cnt)

    for i in range(n):
        before = ''
        cnt = 1
        for j in range(n):
            if before == '':
                before = candies[j][i]
            else:
                now = candies[j][i]
                if now == before:
                    cnt += 1
                    if cnt == n:
                        print(cnt)
                        sys.exit()
                else:
                    result.append(cnt)
                    cnt = 1
                    before = now
        result.append(cnt)
            



def switch_row(candies):
    global n
    for i in range(n):
        for j in range(n - 1):
            if candies[i][j] != candies[i][j + 1]:
                candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
                count_candy(candies)
                candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]


def swtich_col(candies):
    global n

    for i in range(n):
        for j in range(n - 1):
            if candies[j][i] != candies[j + 1][i]:
                candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
                count_candy(candies)
                candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]

def solve(candies):
    count_candy(candies)
    switch_row(candies)
    swtich_col(candies)

candies = []
for _ in range(n):
    candies.append(list(sys.stdin.readline().rstrip()))

solve(candies)
print(max(result))