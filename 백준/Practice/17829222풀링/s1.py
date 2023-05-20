import sys

def do_pooling(li: list):
    res = []
    for i in range(len(li)):
        for j in range(len(li)):
            res.append(li[i][j])
    res.remove(max(res))
    return max(res)

n = int(sys.stdin.readline())

grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))


while len(grid) > 1:
    new_grid = []
    for i in range(0, len(grid), 2):
        tmp = []
        for j in range(0, len(grid[0]), 2):
            tmp.append(do_pooling([row[j:j+2] for row in grid[i:i+2]]))
        new_grid.append(tmp)
    grid = new_grid

print(grid[0][0])

