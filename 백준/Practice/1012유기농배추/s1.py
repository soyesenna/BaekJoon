def m_index(x, m):
    if x < 0:
        return False
    if x > m:
        return False
    
    return True

def n_index(x, n):
    if x < 0:
        return False
    if x > n:
        return False
    
    return True


t = int(input())
result = []
for i in range(t):
    #가로, 세로, 배추개수
    m, n, k = map(int, input().split())

    baechu = []
    jirung = []
    
    for a in range(m):
        tmp = []
        for b in range(n):
            tmp.append(0)
        baechu.append(tmp)

    for a in range(m):
        tmp = []
        for b in range(n):
            tmp.append(0)
        jirung.append(tmp)
    
    for j in range(k):
        col, row = map(int, input().split())
        baechu[col][row] = 1

    for a in range(m):
        for b in range(n):
            if baechu[a][b] == 1:
                if m_index(a-1, m-1):
                    if jirung[a-1][b] == 1 or jirung[a-1][b] == 2:
                        jirung[a][b] = 2
                        continue
                if m_index(a+1, m-1):
                    if jirung[a+1][b] == 1 or jirung[a+1][b] == 2:
                        jirung[a][b] = 2
                        continue
                if n_index(b-1, n-1):
                    if jirung[a][b-1] == 1 or jirung[a][b-1] == 2:
                        jirung[a][b] = 2
                        continue
                if n_index(b+1, n-1):
                    if jirung[a][b+1] == 1 or jirung[a][b+1] == 2:
                        jirung[a][b] = 2
                        continue

                jirung[a][b] = 1
    
    for a in range(m):
        print(jirung[a])
    cnt = 0
    for a in range(m):
        for b in range(n):
            if jirung[a][b] == 1:
                cnt += 1
    result.append(cnt)

for a in range(t):
    print(result[a])
