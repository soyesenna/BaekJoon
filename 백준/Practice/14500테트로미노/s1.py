import sys

input = sys.stdin.readline

n, m = map(int, input().split())

li = []
for _ in range(n):
    li.append(list(map(lambda x: [int(x), False], input().split())))

#위 아래 오른 왼
direction = [[-1,0], [1,0], [0,1], [0,-1]]
result = []
visit = []
def dfs(r,c,cnt):
    global direction, n, m, result, visit
    if cnt == 5:
        visit.pop()
        return li[r][c][0]
    for dir in direction:
        if 0 <= r + dir[0] < n and 0 <= c + dir[1] < m and not li[r+dir[0]][c+dir[1]][1] and [r+dir[0],c+dir[1]] not in visit:
            visit.append([r,c])
            result.append(dfs(r+dir[0], c+dir[1], cnt + 1) + li[r][c][0])
        else:
            continue
    visit.pop()
    return 0


for i in range(n):
     for j in range(m):
        visit = []
        (dfs(i,j,1))
        li[i][j][1] = True
    
print(max(result))