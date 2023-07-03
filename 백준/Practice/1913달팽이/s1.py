import sys


def up(li, x, y, n):
    li[y - 1][x] = n
    return li


def right(li, x, y, n):
    li[y][x + 1] = n
    return li


def down(li, x, y, n):
    li[y + 1][x] = n
    return li


def left(li, x, y, n):
    li[y][x - 1] = n
    return li


n = int(sys.stdin.readline())
target = int(sys.stdin.readline())

li = [[False for _ in range(n)] for _ in range(n)]

flag = 'up'

x = n // 2
y = n // 2
li[y][x] = 1
result = []
if target == 1:
    result.append([x, y])
for i in range(2, n**2 + 1):
    if flag == 'up':
        li = up(li, x, y, i)
        y -= 1
        if not li[y][x + 1]:
            flag = 'right'
    elif flag == 'right':
        li = right(li, x, y, i)
        x += 1
        if not li[y + 1][x]:
            flag = 'down'
    elif flag == 'down':
        li = down(li, x, y, i)
        y += 1
        if not li[y][x - 1]:
            flag = 'left'
    elif flag == 'left':
        li = left(li, x, y, i)
        x -= 1
        if not li[y - 1][x]:
            flag = 'up'

    if target == i:
        result.append([x, y])

for i in range(n):
    for j in range(n):
        print(li[i][j], end=' ')
    print()
print(result[0][1] + 1, result[0][0] + 1)
