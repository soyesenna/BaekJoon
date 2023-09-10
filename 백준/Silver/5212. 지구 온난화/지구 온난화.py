dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def count_sea(x, y, grid):
    count = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == '.':
            count += 1
    return count

def solve(grid):
    new_grid = [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'X':
                if count_sea(i, j, grid) >= 3:
                    new_grid[i][j] = '.'
                else:
                    new_grid[i][j] = 'X'
    return new_grid

R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

grid = solve(grid)

min_x, max_x, min_y, max_y = float('inf'), -float('inf'), float('inf'), -float('inf')
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'X':
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

for i in range(min_x, max_x + 1):
    print(''.join(grid[i][min_y:max_y + 1]))
