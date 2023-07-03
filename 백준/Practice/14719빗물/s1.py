import sys

input = sys.stdin.readline

h, w = map(int, input().split())

li = list(map(int, input().split()))

world = [[0 for _ in range(h)] for _ in range(w)]

for i in range(w):
    for j in range(li[i]):
        world[i][j] = 1

direction = [[-1,0], [1,0], [0,-1]]
for i in range(h):
    for j in range(w):
        if world[j][i] == 1:
            continue
        flag = True
        for dir in direction:
            if not(0 <= j + dir[0] < w):
                flag = False
                break
            if 0 <= i + dir[1] < h and world[j + dir[0]][i + dir[1]] == 0:
                flag = False
                break
        if flag:
            world[j][i] = 2

result = 0
for elem in world:
    result += len(list(filter(lambda x: x == 2, elem)))
print(result)