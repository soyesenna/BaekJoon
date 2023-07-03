import sys

n = int(sys.stdin.readline())

order = sys.stdin.readline().rstrip()

maze = [['#' for _ in range(102)] for _ in range(102)]

now = [51,51]
head = [[1,0], [0,1], [-1, 0], [0,-1]]
now_head = 0
maze[now[0]][now[1]] = '.'
visit = [now[::]]
for i in range(len(order)):
    if order[i] == 'F':
        for j in range(2):
            now[j] += head[now_head][j]
        maze[now[0]][now[1]] = '.'
        visit.append(now[::])
    elif order[i] == 'R':
        now_head -= 1
        if now_head < 0:
            now_head += 4
    elif order[i] == 'L':
        now_head += 1
        if now_head > 3:
            now_head %= 4

visit_row = sorted(visit, key=lambda x:x[0])
visit_row_max = visit_row[-1][0]
visit_row_min = visit_row[0][0]
visit_col = sorted(visit, key=lambda x:x[1])
visit_col_max = visit_col[-1][1]
visit_col_min = visit_col[0][1]

for i in range(visit_row_min, visit_row_max + 1):
    for j in range(visit_col_min, visit_col_max + 1):
        print(maze[i][j], end='')
    print()
