import sys

def col_bingo(bingo):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if bingo[i][j] != False:
                break 
            if j == 4:
                cnt += 1
    return cnt

def row_bingo(bingo):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if bingo[j][i] != False:
                break 
            if j == 4:
                cnt += 1
    return cnt

def right_down_bingo(bingo):
    cnt = 0
    for i in range(5):
        if bingo[i][i] != False:
            break
        if i == 4:
            cnt += 1
    return cnt

def left_down_bingo(bingo):
    cnt = 0
    for i in range(5):
        if bingo[i][4 - i] != False:
            break
        if i == 4:
            cnt += 1
    return cnt


def do_bingo(bingo):
    cnt = 0
    cnt += col_bingo(bingo)
    cnt += row_bingo(bingo)
    cnt += right_down_bingo(bingo)
    cnt += left_down_bingo(bingo)

    if cnt >= 3:
        return True
    
    return False


bingo = []
for _ in range(5):
    bingo.append(list(map(int, sys.stdin.readline().split())))

call_nums = []
for _ in range(5):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in tmp:
        call_nums.append(i)

for n in range(len(call_nums)):
    for i in range(5):
        if call_nums[n] in bingo[i]:
            bingo[i][bingo[i].index(call_nums[n])] = False
    if do_bingo(bingo):
        print(n + 1)
        break
