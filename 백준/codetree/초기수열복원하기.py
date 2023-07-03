import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

for i in range(1, li[0]):
    tmp = [i, li[0] - i]
    for j in range(1, len(li)):
        tmp_num = abs(li[j] - tmp[-1])
        if tmp_num == 0 or tmp_num in tmp:
            break
        tmp.append(tmp_num)
    if len(tmp) == n:
        for res in tmp:
            print(res, end=' ')
        sys.exit()