import sys
import collections

input = sys.stdin.readline

n, k = map(int, input().split())

con = list(map(lambda x: [int(x), False], input().split()))
num_zero = 0
cnt = 0


while num_zero < k:
    cnt += 1
    con = con[-1:]+con[:-1]

    con[n-1][1] = False
    for i in range(len(con) - 1, -1, -1):
        if con[i][1]:
            to_move = i + 1
            if to_move == 2 * n:
                to_move = 0
            if not con[to_move][1] and con[to_move][0] > 0:
                con[i][1] = False
                con[to_move][1] = True
                con[to_move][0] -= 1
                if con[to_move][0] == 0:
                    num_zero += 1
                    if num_zero >= k:
                        print(cnt)
                        sys.exit()
                if to_move == n -1:
                    con[to_move][1] = False
    if con[0][0] > 0:
        con[0][1] = True
        con[0][0] -= 1
        if con[0][0] == 0:
            num_zero += 1

print(cnt)
    