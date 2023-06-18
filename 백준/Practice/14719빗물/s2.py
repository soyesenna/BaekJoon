import sys

input = sys.stdin.readline

h, w = map(int, input().split())

li = list(map(int, input().split()))

world = [[0 for _ in range(h)] for _ in range(w)]

for i in range(w):
    for j in range(li[i]):
        world[i][j] = 1

for i in range(h):
    if world[0][i] == 1 and world[-1][i] == 1:
        if i > 0:
            tmp = []
            for j in range(w):
                tmp.append(world[j][i-1])
            if 0 not in tmp:
                for j in range(w):
                    if world[j][i] == 0:
                        world[j][i] = 2
        else:
            for j in range(w):
                if world[j][i] == 0:
                    world[j][i] = 2

result = 0
for elem in world:
    result += len(list(filter(lambda x: x == 2, elem)))
print(result)