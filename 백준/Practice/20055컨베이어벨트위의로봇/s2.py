import sys

input = sys.stdin.readline

n, k = map(int, input().split())

con = list(map(lambda x: [int(x), False], input().split()))
num_zero = 0
cnt = 0

head = 0

while num_zero < k:
    cnt += 1
    head = (head - 1)
    if head < 0:
        head += 2 * n
    down_potision = (head + n - 1) % (2 * n)
    con[down_potision][1] = False

    to_move = head - 1
    for i in range(2*n):
        to_move = (to_move - i)
        if to_move < 0:
            to_move += 2*n
            to_move %= 2 * n
        if con[to_move][1]:
            if not con[(to_move + 1) % (2 * n)][1] and con[(to_move + 1) % (2 * n)][0] > 0:
                con[to_move][1] = False
                con[(to_move + 1) % (2 * n)][1] = True
                con[(to_move + 1) % (2 * n)][0] -= 1
                if con[(to_move + 1) % (2 * n)][0] == 0:
                    num_zero += 1
        to_move = head - 1
    if con[head][0] > 0:
        con[head][1] = True
        con[head][0] -= 1
        if con[head][0] == 0:
            num_zero += 1

print(cnt)