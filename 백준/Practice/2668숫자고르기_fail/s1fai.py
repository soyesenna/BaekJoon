import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 한도를 늘려줍니다.

def dfs(a, i, j, visited, n, m):
    """
    DFS로 호수를 찾아 부피를 계산합니다.
    """
    dx = [-1, 0, 1, 0] # 위, 오른쪽, 아래, 왼쪽 방향을 나타내는 리스트입니다.
    dy = [0, 1, 0, -1]
    visited[i][j] = True
    volume = a[i][j]
    for k in range(4): # 각 방향으로 이동합니다.
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < n and 0 <= y < m and a[x][y] > 0 and not visited[x][y]:
            volume += dfs(a, x, y, visited, n, m) # 재귀 호출로 호수를 찾아 부피를 계산합니다.
    return volume

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > 0 and not visited[i][j]:
                # 호수를 찾아 부피를 계산합니다.
                volume = dfs(a, i, j, visited, n, m)
                ans = max(ans, volume)
    return ans

t = int(sys.stdin.readline())
result = []
for _ in range(t):
    result.append(solve())

for res in result:
    print(res)