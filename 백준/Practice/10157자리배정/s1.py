from re import L
import sys

def go(li, c, r):
    li[c][r] = True
    return li


r, c = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
if k > r * c:
    print(0)
    sys.exit()

li = [[False for _ in range(r)] for _ in range(c)]

now_c = 0
now_r = 0
flag = 'down'
for i in range(k):
    if flag == 'down':
        li = go(li, now_c, now_r)
        if i == k - 1:
            break
        if now_c == c - 1 or li[now_c + 1][now_r]:
            flag = 'right'
            now_r += 1
        else:
            now_c += 1
    elif flag == 'right':
        li = go(li, now_c, now_r)
        if i == k - 1:
            break
        if now_r == r - 1 or li[now_c][now_r + 1]:
            flag = 'up'
            now_c -= 1
        else:
            now_r += 1
    elif flag == 'up':
        li = go(li, now_c, now_r)
        if i == k - 1:
            break
        if now_c == 0 or li[now_c - 1][now_r]:
            flag = 'left'
            now_r -= 1
        else:
            now_c -= 1
    elif flag == 'left':
        li = go(li, now_c, now_r)
        if i == k - 1:
            break
        if now_r == 0 or li[now_c][now_r - 1]:
            flag = 'down'
            now_c += 1
        else:
            now_r -= 1

print(now_r + 1, now_c + 1)