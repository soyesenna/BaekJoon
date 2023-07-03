import copy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

li = []
for _ in range(n):
    li.append(list(input()))

result = []

def check(sub_cross, r, c):
    global li
    tmp = copy.deepcopy(li)
    for i in range(len(sub_cross)):
        for j in range(len(sub_cross)):
            if li[r - (len(sub_cross) // 2) + i][c - (len(sub_cross) // 2) + j] != sub_cross[i][j]:
                if li[r - (len(sub_cross) // 2) + i][c - (len(sub_cross) // 2) + j] == '.' and sub_cross[i][j] == '*':
                    return False
                elif sub_cross[i][j] == '.':
                    pass
            else:
                if sub_cross[i][j] != '.':
                    tmp[r - (len(sub_cross) // 2) + i][c - (len(sub_cross) // 2) + j] = 'O'
    li = tmp
    return True
    

def find_cross(sub_cross):
    global li
    global n, m
    global result
    for i in range(len(sub_cross) // 2, n - (len(sub_cross) // 2) + 1):
        for j in range(len(sub_cross) // 2, m - (len(sub_cross) // 2) + 1):
            if check(sub_cross, i, j):
                result.append([i + 1, j + 1, len(sub_cross) // 2])
    
max_cross = min(n, m)
if max_cross % 2 == 0:
    max_cross -= 1

for i in range(3, max_cross + 1, 2):
    sub_cross = []
    for j in range(i):
        tmp = []
        for k in range(i):
            if j == i // 2:
                tmp.append("*")
                continue
            if k == i // 2:
                tmp.append("*")
            else:
                tmp.append(".")
        sub_cross.append(tmp)
    find_cross(sub_cross)

for i in range(len(li)):
    if '*' in li[i]:
        print(-1)
        sys.exit()

print(len(result))
for res in result:
    for r in res:
        print(r, end= ' ')
    print()