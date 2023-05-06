def m_index(x, m):
    if x < 0:
        return False
    if x > m-1:
        return False
    
    return True

def n_index(x, n):
    if x < 0:
        return False
    if x > n-1:
        return False
    
    return True


t = int(input())
result = []
for i in range(t):
    #가로, 세로, 배추개수
    m, n, k = map(int, input().split())

    baechu = []
    
    
    for a in range(m):
        tmp = []
        for b in range(n):
            tmp.append(0)
        baechu.append(tmp)
    
    for j in range(k):
        col, row = map(int, input().split())
        baechu[col][row] = 1

    cnt=0
    flag = True
    while flag:
        road = list()
        for a in range(m):
            for b in range(n):
                if baechu[a][b] == 1:
                    road.append([a,b])
                    baechu[a][b] = 2
                    cnt += 1
                    break
            if baechu[a][b] == 2:
                break
            if a == m-1 and b == n-1:
                flag = False
                continue
        a = 0
        while True:
            if m_index(road[a][0]-1, m):
                if baechu[road[a][0]-1][road[a][1]] == 1:
                    if not [road[a][0]-1, road[a][1]] in road:
                        road.append([road[a][0]-1, road[a][1]])
                        baechu[road[a][0]-1][road[a][1]] = 2
            if m_index(road[a][0]+1, m):
                if baechu[road[a][0]+1][road[a][1]] == 1:
                    if not [road[a][0]+1, road[a][1]] in road:
                        road.append([road[a][0]+1, road[a][1]])
                        baechu[road[a][0]+1][road[a][1]] = 2
            if n_index(road[a][1]-1, n):
                if baechu[road[a][0]][road[a][1]-1] == 1:
                    if not [road[a][0], road[a][1]-1] in road:
                        road.append([road[a][0], road[a][1]-1])
                        baechu[road[a][0]][road[a][1]-1] = 2
            if n_index(road[a][1]+1, n):
                if baechu[road[a][0]][road[a][1]+1] == 1:
                    if not [road[a][0], road[a][1]+1] in road:
                        road.append([road[a][0], road[a][1]+1])
                        baechu[road[a][0]][road[a][1]+1] = 2
            if a >= len(road)-1:
                break
                
            a += 1
        
        
    result.append(cnt)

for i in range(t):
    print(result[i])